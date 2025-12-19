import time
from strategies import ai_analysis
from config import PAIRS, CHECK_INTERVAL_SECONDS
from utils import send_signal


def run_engine():
    print("🚀 Aquila AI Engine Started")

    while True:
        signals_count = 0

        for pair in PAIRS:
            signal = ai_analysis(pair, "1m")

            if signal:
                send_signal(signal)
                signals_count += 1
                time.sleep(2)

        print(f"✅ Scan finished | Signals found: {signals_count}")
        time.sleep(CHECK_INTERVAL_SECONDS)
