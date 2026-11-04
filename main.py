import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "សួស្តី! ❤️\n"
        "Welcome to my Telegram Auto Reply Bot!\n\n"
        "អ្នកអាចជជែកជាមួយខ្ញុំជាភាសាខ្មែរ និង English។"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 BOT HELP MENU\n\n"
        "សួស្តី = ជំរាបសួរ!\n"
        "Hi = Hello!\n"
        "How are you = I'm fine!\n"
        "Thank you = You're welcome!\n"
        "Bye = Goodbye!\n"
    )


async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.lower()

    if "សួស្តី" in msg or "ជំរាបសួរ" in msg:
        reply = "ជំរាបសួរ! ❤️ តើខ្ញុំអាចជួយអ្វីអ្នកបាន?"

    elif "hi" in msg or "hello" in msg:
        reply = "Hello! 👋 How can I help you?"

    elif "how are you" in msg:
        reply = "I'm fine! Thank you. 😊"

    elif "thank" in msg:
        reply = "You're welcome! ❤️"

    elif "bye" in msg:
        reply = "Goodbye! Have a nice day! 👋"

    else:
        reply = "សូមអរគុណដែលបានផ្ញើសារ! ❤️\nPlease type /help for assistance."

    await update.message.reply_text(reply)


def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN is missing!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply)
    )

    print("Telegram Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
