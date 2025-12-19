from flask import Flask, render_template, request, redirect
from utils import load_settings, save_settings

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def dashboard():
    settings = load_settings()

    if request.method == "POST":
        settings["enabled"] = "enabled" in request.form
        settings["pairs"] = request.form["pairs"].split(",")
        settings["timeframe"] = request.form["timeframe"]
        settings["strategy"] = request.form["strategy"]
        save_settings(settings)
        return redirect("/")

    return render_template(
        "dashboard.html",
        enabled=settings["enabled"],
        pairs=settings["pairs"],
        timeframe=settings["timeframe"],
        strategy=settings["strategy"]
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
