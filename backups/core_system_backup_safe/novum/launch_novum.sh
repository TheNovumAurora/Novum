#!/data/data/com.termux/files/usr/bin/bash
# Launch Novum Aurora and open browser automatically

cd "$(dirname "$0")" || exit 1

# Run the Flask web interface in the background
./run_web.sh &

# Give Flask a few seconds to start
sleep 3

# Open the preferred browser on Android via Termux
# termux-open-url will open the default browser
termux-open-url "http://127.0.0.1:5000"
