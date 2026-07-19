import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("8278568972:AAG5zdQq6nIo4X1WvjNk6ZS4EUeyGDIentg")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salom! 👋\n"
        "Bot muvaffaqiyatli ishlayapti ✅"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot ishga tushdi!")
    app.run_polling()


if __name__ == "__main__":
    main()
