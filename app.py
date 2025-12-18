from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

def is_bot_running():
    result = subprocess.getoutput("pgrep -f main.py")
    return bool(result)

@app.route("/")
def dashboard():
    status = "🟢 Running" if is_bot_running() else "🔴 Stopped"
    return render_template("dashboard.html", status=status)

@app.route("/start")
def start_bot():
    subprocess.Popen("cd ~/aquila_bot && source venv/bin/activate && nohup python3 main.py &", shell=True)
    return redirect(url_for("dashboard"))

@app.route("/stop")
def stop_bot():
    subprocess.call("pkill -f main.py", shell=True)
    return redirect(url_for("dashboard"))

@app.route("/restart")
def restart_bot():
    subprocess.call("pkill -f main.py", shell=True)
    subprocess.Popen("cd ~/aquila_bot && source venv/bin/activate && nohup python3 main.py &", shell=True)
    return redirect(url_for("dashboard"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
