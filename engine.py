# -*- coding: utf-8 -*-

import time, random, asyncio
import state
from config import PAIRS, DEFAULT_TIMEFRAMES, PAIR_TIMEFRAMES

def ai_analysis(pair, tf):
    if random.randint(1, 15) == 7:
        return {
            "pair": pair,
            "tf": tf,
            "dir": random.choice(["BUY", "SELL"]),
            "strength": random.randint(55, 90),
            "conf": random.randint(70, 95)
        }

async def send_signal(sig):
    print(f"📢 SIGNAL {sig}")

def run_engine():
    print("🚀 Engine Started")

    while True:
        if not state.BOT_RUNNING:
            time.sleep(5)
            continue

        count = 0
        for pair in PAIRS:
            if state.ACTIVE_PAIRS and pair not in state.ACTIVE_PAIRS:
                continue

            tfs = PAIR_TIMEFRAMES.get(pair, DEFAULT_TIMEFRAMES)
            if state.ACTIVE_TIMEFRAME:
                tfs = [state.ACTIVE_TIMEFRAME]

            for tf in tfs:
                sig = ai_analysis(pair, tf)
                if sig:
                    asyncio.run(send_signal(sig))
                    count += 1
                    time.sleep(2)

        print(f"✅ Scan finished | Signals: {count}")
        time.sleep(300)

if __name__ == "__main__":
    run_engine()
