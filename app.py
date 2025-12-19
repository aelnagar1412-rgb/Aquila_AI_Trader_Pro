from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)
SETTINGS_FILE = "settings.json"


def load_settings():
    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_settings(data):
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


@app.route("/")
def dashboard():
    settings = load_settings()

    return render_template(
        "dashboard.html",
        enabled=settings.get("enabled", False),
        pairs=settings.get("pairs", []),
        timeframe=settings.get("timeframe", "1m"),
        strategy=settings.get("strategy", "RSI_EMA")
    )


@app.route("/update_pairs", methods=["POST"])
def update_pairs():
    settings = load_settings()

    pairs_input = request.form.get("pairs", "")
    pairs = [p.strip().upper() for p in pairs_input.split(",") if p.strip()]

    settings["pairs"] = pairs
    save_settings(settings)

    return redirect(url_for("dashboard"))


@app.route("/toggle")
def toggle_bot():
    settings = load_settings()
    settings["enabled"] = not settings["enabled"]
    save_settings(settings)
    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
