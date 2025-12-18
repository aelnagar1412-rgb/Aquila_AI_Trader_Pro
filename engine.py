# ===============================
# Aquila AI Trader Pro - Engine
# ===============================

from datetime import datetime
from config import (
    ENABLE_FOREX,
    ENABLE_OTC,
    AUTO_MARKET,
    AI_MIN_SCORE,
    TIMEFRAMES
)

from strategies import analyze_pair
from ai_filter import ai_filter_decision
from utils import log_info


# ===============================
# الأزواج
# ===============================

FOREX_PAIRS = [
    "EURUSD", "GBPUSD", "USDJPY", "AUDUSD",
    "USDCAD", "USDCHF", "NZDUSD"
]

OTC_PAIRS = [
    "EURUSD-OTC", "GBPUSD-OTC", "USDJPY-OTC"
]


# ===============================
# Auto Market Detector
# ===============================

def detect_market():
    hour = datetime.utcnow().hour
    # OTC غالبًا بيبقى خارج أوقات السوق
    if hour < 7 or hour > 20:
        return "OTC"
    return "FOREX"


# ===============================
# Engine Runner
# ===============================

def run_engine():
    log_info("🔍 Starting market scan")

    market = detect_market() if AUTO_MARKET else "FOREX"

    pairs = []
    if market == "FOREX" and ENABLE_FOREX:
        pairs = FOREX_PAIRS
    elif market == "OTC" and ENABLE_OTC:
        pairs = OTC_PAIRS

    signals = []

    for pair in pairs:
        for tf in TIMEFRAMES:
            result = analyze_pair(pair, tf)
            if not result:
                continue

            # AI Final Filter
            if ai_filter_decision(result, AI_MIN_SCORE):
                signals.append(result)

    log_info(f"✅ Scan finished | Signals found: {len(signals)}")
    return signals
