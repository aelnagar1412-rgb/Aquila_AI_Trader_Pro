import random

def ai_analysis(pair, timeframe):
    """
    Strong 1m Strategy (Mocked)
    EMA Trend + RSI Filter
    """

    rsi = random.randint(30, 70)
    ema_fast = random.randint(1, 100)
    ema_slow = random.randint(1, 100)

    strength = random.randint(50, 90)

    # BUY conditions
    if ema_fast > ema_slow and rsi > 55 and strength >= 60:
        return {
            "pair": pair,
            "timeframe": timeframe,
            "direction": "BUY",
            "strength": strength,
            "reason": "EMA Uptrend + RSI > 55"
        }

    # SELL conditions
    if ema_fast < ema_slow and rsi < 45 and strength >= 60:
        return {
            "pair": pair,
            "timeframe": timeframe,
            "direction": "SELL",
            "strength": strength,
            "reason": "EMA Downtrend + RSI < 45"
        }

    return None
