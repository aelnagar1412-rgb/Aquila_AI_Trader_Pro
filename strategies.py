import random

def ai_analysis(pair, timeframe):
    """
    RSI + EMA Trend Strategy (Mock logic for now)
    Replace price feed later
    """

    # محاكاة (عشان البوت يشتغل)
    signal_chance = random.randint(1, 100)

    if signal_chance > 92:
        return {
            "pair": pair,
            "timeframe": timeframe,
            "direction": "BUY",
            "strength": random.randint(60, 85),
            "confidence": random.randint(80, 95),
            "reason": "RSI + EMA Trend"
        }

    if signal_chance < 8:
        return {
            "pair": pair,
            "timeframe": timeframe,
            "direction": "SELL",
            "strength": random.randint(60, 85),
            "confidence": random.randint(80, 95),
            "reason": "RSI + EMA Trend"
        }

    return None
