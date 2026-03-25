#!/data/data/com.termux/files/usr/bin/bash

# Move to the system root
cd ~/core_system || exit

# Kill any previous Flask server
pkill -f interface.web 2>/dev/null

# Start Flask as a module (fixed imports)
python3 -m interface.web &

# Give it a moment to boot
sleep 2

# Open browser
termux-open-url http://127.0.0.1:5000
