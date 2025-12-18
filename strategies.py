# ===============================
# Aquila AI Trader Pro - Strategies
# ===============================

import random
from datetime import datetime


# ===============================
# أدوات مساعدة
# ===============================

def _score(value, max_score):
    return min(max_score, max(0, value))


# ===============================
# Strategy 1: Trend
# ===============================

def trend_strategy(pair, timeframe):
    direction = random.choice(["BUY", "SELL"])
    strength = _score(random.randint(15, 30), 30)
    reason = f"Trend shows {direction} dominance on {timeframe}"
    return direction, strength, reason


# ===============================
# Strategy 2: Momentum
# ===============================

def momentum_strategy(pair, timeframe):
    direction = random.choice(["BUY", "SELL"])
    strength = _score(random.randint(10, 25), 25)
    reason = f"Momentum accelerating {direction} on {timeframe}"
    return direction, strength, reason


# ===============================
# Strategy 3: Breakout
# ===============================

def breakout_strategy(pair, timeframe):
    direction = random.choice(["BUY", "SELL"])
    strength = _score(random.randint(20, 35), 35)
    reason = f"Price breakout confirmed ({direction}) on {timeframe}"
    return direction, strength, reason


# ===============================
# Strategy 4: Mean Reversion
# ===============================

def mean_reversion_strategy(pair, timeframe):
    direction = random.choice(["BUY", "SELL"])
    strength = _score(random.randint(5, 20), 20)
    reason = f"Mean reversion setup ({direction}) on {timeframe}"
    return direction, strength, reason


# ===============================
# Strategy 5: Time Bias
# ===============================

def time_bias_strategy(pair, timeframe):
    hour = datetime.utcnow().hour
    direction = "BUY" if hour % 2 == 0 else "SELL"
    strength = 15
    reason = f"Time bias favors {direction} at hour {hour}"
    return direction, strength, reason


# ===============================
# Strategy Engine (Voting System)
# ===============================

def analyze_pair(pair, timeframe):
    strategies = [
        trend_strategy,
        momentum_strategy,
        breakout_strategy,
        mean_reversion_strategy,
        time_bias_strategy
    ]

    buy_score = 0
    sell_score = 0
    reasons = []

    for strat in strategies:
        direction, strength, reason = strat(pair, timeframe)
        reasons.append(reason)

        if direction == "BUY":
            buy_score += strength
        else:
            sell_score += strength

    if buy_score == sell_score:
        return None  # لا يوجد اتجاه واضح

    direction = "BUY" if buy_score > sell_score else "SELL"
    total_score = abs(buy_score - sell_score)

    return {
        "pair": pair,
        "timeframe": timeframe,
        "direction": direction,
        "score": total_score,
        "reasons": reasons,
        "strategies_used": len(strategies)
    }
