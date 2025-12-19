# ===============================
# Aquila AI Trader Pro - Config
# ===============================

# ---------- BOT ----------
BOT_NAME = "Aquila AI Trader Pro"
BOT_TOKEN = "8570409684:AAEQBhKv0zMZaEXWcoCUGiJsKRspE5JuleM"

# ---------- LANGUAGE ----------
LANG = "ar"   # ar / en

# ---------- ENGINE ----------
CHECK_INTERVAL_SECONDS = 60
ENABLE_NO_SIGNAL_ALERT = False   # يمنع رسالة "لا توجد إشارات"

# ---------- TIMEFRAME ----------
DEFAULT_TIMEFRAME = "1m"

# ---------- PAIRS ----------
PAIRS = [
    "EURUSD",
    "EURJPY",
    "EURGBP",
    "AUDCAD",
    "USDJPY"
]

# ---------- SIGNAL FILTERS ----------
MIN_SIGNAL_STRENGTH = 50
MIN_AI_CONFIDENCE = 0.75
MAX_SIGNALS_PER_SCAN = 5

# ---------- DASHBOARD ----------
DASHBOARD_HOST = "0.0.0.0"
DASHBOARD_PORT = 5000

# ---------- LOGGING ----------
LOG_LEVEL = "INFO"
