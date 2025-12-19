# -*- coding: utf-8 -*-

import time
import asyncio
import state
from config import PAIRS, DEFAULT_TIMEFRAMES, PAIR_TIMEFRAMES

# ======================
# AI ANALYSIS (تجريبي)
# ======================
def ai_analysis(pair, tf):
    import random
    if random.randint(1, 20) == 10:
        return {
            "pair": pair,
            "tf": tf,
            "direction": "BUY",
            "strength": random.randint(50, 90),
            "confidence": random.randint(70, 95)
        }
    return None


async def send_signal(signal):
    print(f"📢 SIGNAL => {signal}")


# ======================
# ENGINE LOOP
# ======================
def run_engine():
    print("🚀 Aquila AI Trader Pro Engine Started")

    while True:

        if not state.BOT_RUNNING:
            time.sleep(5)
            continue

        signals_count = 0

        for pair in PAIRS:

            if state.ACTIVE_PAIRS and pair not in state.ACTIVE_PAIRS:
                continue

            timeframes = PAIR_TIMEFRAMES.get(pair, DEFAULT_TIMEFRAMES)

            if state.ACTIVE_TIMEFRAME:
                timeframes = [state.ACTIVE_TIMEFRAME]

            for tf in timeframes:
                signal = ai_analysis(pair, tf)
                if signal:
                    asyncio.run(send_signal(signal))
                    signals_count += 1
                    time.sleep(2)

        print(f"✅ Scan finished | Signals found: {signals_count}")
        time.sleep(300)


if __name__ == "__main__":
    run_engine()
