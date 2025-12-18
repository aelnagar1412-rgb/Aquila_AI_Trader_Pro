# ===============================
# Aquila AI Trader Pro - AI Filter
# ===============================

def ai_filter_decision(signal, min_score):
    """
    فلتر ذكي نهائي
    يعتمد على:
    - قوة الإشارة
    - عدد الاستراتيجيات
    """

    score = signal.get("score", 0)
    strategies_used = signal.get("strategies_used", 0)

    # شروط القبول
    MIN_STRATEGIES_REQUIRED = 3

    if score >= min_score and strategies_used >= MIN_STRATEGIES_REQUIRED:
        signal["ai_status"] = "APPROVED"
        signal["ai_confidence"] = min(
            95,
            60 + (score // 2)
        )
        return True

    signal["ai_status"] = "REJECTED"
    signal["ai_confidence"] = max(10, score)
    return False
