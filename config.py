# ===============================
# Aquila AI Trader Pro - Config
# ===============================

# --- Bot Info ---
BOT_NAME = "Aquila AI Trader Pro"
BOT_TOKEN = "8570409684:AAEQBhKv0zMZaEXWcoCUGiJsKRspE5JuleM"

# --- Language ---
LANG = "ar"   # ar / en

# --- Engine Settings ---
CHECK_INTERVAL_SECONDS = 60   # scan every 60 seconds

# --- Trading Settings ---
DEFAULT_TIMEFRAME = "1m"

PAIRS = [
    "EURUSD",
    "EURJPY",
    "EURGBP",
    "AUDCAD",
    "USDJPY"
]

# --- Signal Filters ---
MIN_SIGNAL_STRENGTH = 50
MIN_AI_CONFIDENCE = 0.75

# --- Risk / Limits ---
MAX_SIGNALS_PER_SCAN = 5

# --- Dashboard ---
DASHBOARD_HOST = "0.0.0.0"
DASHBOARD_PORT = 5000

# --- Logging ---
LOG_LEVEL = "INFO"
