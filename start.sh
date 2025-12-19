#!/bin/bash

echo "🚀 Starting Aquila AI Trader Pro..."

# وقف أي تشغيل قديم
pkill -f engine.py
pkill -f main.py
pkill -f gunicorn

sleep 2

# تشغيل Engine (التحليل + الإشارات)
nohup python3 engine.py > aquila.log 2>&1 &

sleep 2

# تشغيل لوحة التحكم (Dashboard)
nohup python3 app.py > panel.log 2>&1 &

echo "✅ Aquila AI Trader Pro Started"
echo "📊 Dashboard: http://SERVER_IP:5000"
