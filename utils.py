import json

FILE = "settings.json"

def load_settings():
    with open(FILE, "r") as f:
        return json.load(f)

def save_settings(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=2))
