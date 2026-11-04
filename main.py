import os
import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
SECRET = os.getenv("WEBHOOK_SECRET")
PORT = int(os.getenv("PORT", "10000"))
URL = os.getenv("RENDER_EXTERNAL_URL")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "សួស្តី! 👋\n"
        "ខ្ញុំជា Telegram Auto Reply Bot 🤖\n"
        "សូមផ្ញើសារមកខ្ញុំ!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "របៀបប្រើ Bot:\n"
        "/start - ចាប់ផ្តើម\n"
        "/help - ជំនួយ"
    )


async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text

    await update.message.reply_text(
        f"🤖 អ្នកបានផ្ញើសារ៖\n{message}\n\n"
        "អរគុណដែលបានទាក់ទងមកខ្ញុំ! ❤️"
    )


def main():
    if not TOKEN:
        raise RuntimeError("Missing TELEGRAM_BOT_TOKEN")

    if not SECRET:
        raise RuntimeError("Missing WEBHOOK_SECRET")

    if not URL:
        raise RuntimeError("Missing RENDER_EXTERNAL_URL")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply)
    )

    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=SECRET,
        webhook_url=f"{URL.rstrip('/')}/{SECRET}",
        secret_token=SECRET,
        allowed_updates=Update.ALL_TYPES
    )


if __name__ == "__main__":
    main()
