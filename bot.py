# -*- coding: utf-8 -*-
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import state

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Aquila AI Bot Started")

async def set_tf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❌ /tf 1m | 5m | 15m")
        return
    state.ACTIVE_TIMEFRAME = context.args[0]
    state.persist()
    await update.message.reply_text(f"⏱ Timeframe set to {state.ACTIVE_TIMEFRAME}")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🟢 Running: {state.BOT_RUNNING}\n"
        f"⏱ TF: {state.ACTIVE_TIMEFRAME}\n"
        f"💱 Pairs: {state.ACTIVE_PAIRS or 'ALL'}"
    )

def send_signal_telegram(app, text):
    app.bot.send_message(chat_id=app.chat_id, text=text)
