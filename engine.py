import time
from strategies import ai_analysis
from utils import send_signal
import json

SETTINGS_FILE = "settings.json"

def load_settings():
    with open(SETTINGS_FILE) as f:
        return json.load(f)

def run_engine():
    print("🚀 Engine Started")

    while True:
        settings = load_settings()
        tf = settings["timeframe"]

        for pair in settings["pairs"]:
            signal = ai_analysis(pair, tf)
            if signal:
                send_signal(signal)
                time.sleep(2)

        time.sleep(60)
