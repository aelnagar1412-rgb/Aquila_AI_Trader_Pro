# ===============================
# Aquila AI Trader Pro - Utils
# ===============================

from datetime import datetime

LOG_FILE = "aquila.log"


def log_info(message):
    _write_log("INFO", message)


def log_error(message):
    _write_log("ERROR", message)


def _write_log(level, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] [{level}] {message}"
    print(line)

    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass
