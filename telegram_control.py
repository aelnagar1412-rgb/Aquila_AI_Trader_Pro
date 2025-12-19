from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import json

SETTINGS_FILE = "settings.json"

def load_settings():
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def save_settings(data):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Aquila AI Bot Online")

async def tf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    settings = load_settings()
    tf = context.args[0]
    settings["timeframe"] = tf
    save_settings(settings)
    await update.message.reply_text(f"⏱️ Timeframe set to {tf}")

async def pairs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    settings = load_settings()
    pairs = ",".join(settings["pairs"])
    await update.message.reply_text(f"📊 Active pairs:\n{pairs}")

def start_bot(token):
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tf", tf))
    app.add_handler(CommandHandler("pairs", pairs))

    app.run_polling()
