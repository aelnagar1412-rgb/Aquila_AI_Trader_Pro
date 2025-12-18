# ===============================
# Aquila AI Trader Pro - Config
# ===============================

# 🤖 Bot Info
BOT_NAME = "🦅 Aquila AI Trader Pro"

# 🔑 Telegram
BOT_TOKEN = "8570409684:AAEQBhKv0zMZaEXWcoCUGiJsKRspE5JuleM"
CHAT_ID = 818760257  # غيره لو محتاج

# 🌍 Language
# AR / EN / BOTH
LANG = "BOTH"

# ⏱️ Timeframes
TIMEFRAMES = ["1m", "5m"]

# 🔁 Check interval (seconds)
CHECK_INTERVAL_SECONDS = 300  # كل 5 دقائق

# 📊 Markets
ENABLE_FOREX = True
ENABLE_OTC = True
AUTO_MARKET = True

# 🧠 AI Filter
AI_MIN_SCORE = 40

# ⚠️ Alerts
ENABLE_NO_SIGNAL_ALERT = True

# 📈 Trade Settings (إشارات فقط)
DEFAULT_EXPIRY_MINUTES = {
    "1m": 3,
    "5m": 5
}
