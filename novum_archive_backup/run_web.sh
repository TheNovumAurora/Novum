#!/data/data/com.termux/files/usr/bin/bash
cd "$(dirname "$0")" || exit 1

# Set Python path so imports work
export PYTHONPATH="$PWD"

# Start Flask server
python3 interface/web.py
