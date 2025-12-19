import time
import json
import asyncio

from analysis import ai_analysis
from telegram_bot import send_signal

SETTINGS_FILE = "settings.json"


def load_settings():
    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def run_engine():
    print("🚀 Aquila AI Trader Pro Engine Started")

    while True:
        try:
            settings = load_settings()

            if not settings.get("enabled", False):
                time.sleep(5)
                continue

            pairs = settings.get("pairs", [])
            timeframes = settings.get("timeframes", [])
            min_strength = settings.get("min_strength", 50)
            scan_interval = settings.get("scan_interval", 60)

            signals_count = 0

            for pair in pairs:
                for tf in timeframes:
                    signal = ai_analysis(pair, tf)

                    if signal and signal.get("strength", 0) >= min_strength:
                        asyncio.run(send_signal(signal))
                        signals_count += 1
                        time.sleep(2)

            print(f"✅ Scan finished | Signals found: {signals_count}")
            time.sleep(scan_interval)

        except Exception as e:
            print(f"❌ Engine error: {e}")
            time.sleep(5)


if __name__ == "__main__":
    run_engine()
