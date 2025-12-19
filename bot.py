from telegram import Bot
from utils import load_settings

def send_message(text):
    s = load_settings()
    bot = Bot(token=s["bot_token"])
    bot.send_message(chat_id=s["chat_id"], text=text)
