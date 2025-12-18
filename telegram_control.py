# ===============================
# Aquila AI Trader Pro - Telegram
# ===============================

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes
)

from config import BOT_TOKEN, CHAT_ID, BOT_NAME, LANG
from utils import log_info


# ===============================
# رسائل مساعدة
# ===============================

def _lang(ar, en):
    if LANG == "AR":
        return ar
    if LANG == "EN":
        return en
    return f"{ar}\n{en}"


# ===============================
# أوامر تيليجرام
# ===============================

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = _lang(
        "🦅 أهلاً بك في Aquila AI Trader Pro\n\n"
        "/status - حالة البوت\n"
        "/help - المساعدة",
        "🦅 Welcome to Aquila AI Trader Pro\n\n"
        "/status - Bot status\n"
        "/help - Help"
    )
    await update.message.reply_text(msg)


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = _lang(
        "📌 الأوامر المتاحة:\n"
        "/status - حالة البوت\n",
        "📌 Available commands:\n"
        "/status - Bot status\n"
    )
    await update.message.reply_text(msg)


async def cmd_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = _lang(
        "🟢 البوت يعمل الآن ويفحص السوق كل 5 دقائق",
        "🟢 Bot is running and scanning market every 5 minutes"
    )
    await update.message.reply_text(msg)


# ===============================
# إرسال الإشارات
# ===============================

async def send_signal_message(signal):
    text = _lang(
        f"""
📈 إشارة تداول جديدة
------------------
الزوج: {signal['pair']}
الفريم: {signal['timeframe']}
الاتجاه: {signal['direction']}
قوة الإشارة: {signal['score']}
ثقة AI: {signal.get('ai_confidence')}%

الأسباب:
""" + "\n".join(f"- {r}" for r in signal["reasons"]),
        f"""
📈 New Trading Signal
------------------
Pair: {signal['pair']}
Timeframe: {signal['timeframe']}
Direction: {signal['direction']}
Strength: {signal['score']}
AI Confidence: {signal.get('ai_confidence')}%

Reasons:
""" + "\n".join(f"- {r}" for r in signal["reasons"])
    )

    await _app.bot.send_message(chat_id=CHAT_ID, text=text)


async def send_no_signal_message():
    text = _lang(
        "⛔ لا توجد فرص تداول قوية حالياً",
        "⛔ No strong trading opportunities at the moment"
    )
    await _app.bot.send_message(chat_id=CHAT_ID, text=text)


# ===============================
# تشغيل البوت
# ===============================

_app = None

async def start_bot():
    global _app
    _app = ApplicationBuilder().token(BOT_TOKEN).build()

    _app.add_handler(CommandHandler("start", cmd_start))
    _app.add_handler(CommandHandler("help", cmd_help))
    _app.add_handler(CommandHandler("status", cmd_status))

    log_info("📲 Telegram Bot Started")
    await _app.initialize()
    await _app.start()
    await _app.bot.initialize()
