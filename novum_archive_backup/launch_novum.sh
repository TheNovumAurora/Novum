#!/data/data/com.termux/files/usr/bin/bash
# Launch Novum Aurora and open browser automatically

cd "$(dirname "$0")" || exit 1

# Run the Flask web interface in the background
./run_web.sh &

python3 -m novum.main &

sleep 3

if command -v termux-open-url >/dev/null 2>&1; then
    termux-open-url http://127.0.0.1:5000
elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open http://127.0.0.1:5000
elif command -v open >/dev/null 2>&1; then
    open http://127.0.0.1:5000
else
    echo "Open browser: http://127.0.0.1:5000"
fi
