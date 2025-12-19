from flask import Flask, render_template, request
import json

app = Flask(__name__)
SETTINGS_FILE = "settings.json"

def load_settings():
    with open(SETTINGS_FILE) as f:
        return json.load(f)

def save_settings(data):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/", methods=["GET", "POST"])
def dashboard():
    settings = load_settings()

    if request.method == "POST":
        pairs = request.form.get("pairs")
        settings["pairs"] = pairs.split(",")
        save_settings(settings)

    return render_template("dashboard.html", settings=settings)

app.run(host="0.0.0.0", port=5000)
