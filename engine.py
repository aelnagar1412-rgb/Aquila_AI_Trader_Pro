import time
from utils import load_settings

def run_engine():
    print("🚀 Aquila Engine Started")

    while True:
        s = load_settings()

        if not s["enabled"]:
            time.sleep(3)
            continue

        print(f"Running {s['strategy']} on {s['pairs']} TF {s['timeframe']}")
        time.sleep(10)
