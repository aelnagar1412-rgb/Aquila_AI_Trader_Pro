# -*- coding: utf-8 -*-
import json

SETTINGS_FILE = "settings.json"

def load():
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def save(data):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=2)

data = load()

BOT_RUNNING = data["bot_running"]
ACTIVE_TIMEFRAME = data["timeframe"]
ACTIVE_PAIRS = data["pairs"]

def persist():
    save({
        "bot_running": BOT_RUNNING,
        "timeframe": ACTIVE_TIMEFRAME,
        "pairs": ACTIVE_PAIRS
    })
