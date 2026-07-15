from flask import Flask
from telegram import Bot
import os

app = Flask(__name__)

TOKEN = os.environ.get("8278568972:AAGK-eFHDxAasYfb81Vw3K4jTZKvFycHbao")
CHAT_ID = os.environ.get("5799767418")

bot = Bot(8278568972:AAGK-eFHDxAasYfb81Vw3K4jTZKvFycHbao)

@app.route("/")
def home():
    return "Bot ishlayapti!"

@app.route("/test")
def test():
    bot.send_message(
        chat_id=CHAT_ID,
        text="✅ XAUUSD signal bot ishlayapti!"
    )
    return "Xabar yuborildi"
