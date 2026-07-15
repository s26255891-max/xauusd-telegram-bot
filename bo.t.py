from flask import Flask
from telegram import Bot

TOKEN = "8278568972:AAH5k5_t-ygko9hTVXH9yOEhPrH2K-8MYlU"
CHAT_ID = "8278568972"

app = Flask(__name__)
bot = Bot(token=TOKEN)

@app.route("/")
def home():
    return "Bot ishlayapti!"

@app.route("/test")
def test():
    bot.send_message(chat_id=CHAT_ID, text="✅ Bot ishlayapti!")
    return "Xabar yuborildi!"
