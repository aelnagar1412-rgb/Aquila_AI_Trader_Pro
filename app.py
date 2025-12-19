# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
import state, os, signal

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        running=state.BOT_RUNNING,
        tf=state.ACTIVE_TIMEFRAME,
        pairs=state.ACTIVE_PAIRS
    )

@app.route("/start")
def start():
    state.BOT_RUNNING = True
    state.persist()
    return redirect("/")

@app.route("/stop")
def stop():
    state.BOT_RUNNING = False
    state.persist()
    return redirect("/")

@app.route("/restart")
def restart():
    os.kill(os.getpid(), signal.SIGTERM)

@app.route("/set_tf", methods=["POST"])
def set_tf():
    state.ACTIVE_TIMEFRAME = request.form.get("tf") or None
    state.persist()
    return redirect("/")

@app.route("/set_pairs", methods=["POST"])
def set_pairs():
    state.ACTIVE_PAIRS = request.form.getlist("pairs")
    state.persist()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
