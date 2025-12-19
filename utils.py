from telegram import Bot
from config import BOT_TOKEN, CHAT_ID

bot = Bot(token=BOT_TOKEN)

def send_signal(signal):
    text = f"""
📊 إشارة جديدة
الزوج: {signal['pair']}
الفريم: {signal['timeframe']}
الاتجاه: {signal['direction']}
القوة: {signal['strength']}
السبب: {signal['reason']}
"""
    bot.send_message(chat_id=CHAT_ID, text=text)
