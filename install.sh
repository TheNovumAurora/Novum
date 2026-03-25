#!/usr/bin/env bash

echo "🚀 Installing Novum..."

INSTALL_DIR="$HOME/novum"

# Detect package manager
install_deps() {
    if command -v pkg >/dev/null 2>&1; then
        echo "📱 Termux detected"
        pkg update -y
        pkg install -y python git curl
    elif command -v apt >/dev/null 2>&1; then
        echo "🐧 Linux detected"
        sudo apt update -y
        sudo apt install -y python3 python3-pip git curl
    elif command -v brew >/dev/null 2>&1; then
        echo "🍎 Mac detected"
        brew install python git curl
    else
        echo "⚠️ Unknown system. Install python3, git, curl manually."
    fi
}

install_deps

# Clone or update
if [ -d "$INSTALL_DIR" ]; then
    echo "🔄 Updating Novum..."
    cd "$INSTALL_DIR"
    git pull
else
    echo "📦 Cloning Novum..."
    git clone https://github.com/TheNovumAurora/novum.git "$INSTALL_DIR"
    cd "$INSTALL_DIR"
fi

# Install python deps
pip3 install -r requirements.txt 2>/dev/null || pip install -r requirements.txt

echo "🔥 Launching Novum..."

python3 -m novum.main &

sleep 3

# Open browser cross-platform
if command -v termux-open-url >/dev/null 2>&1; then
    termux-open-url http://127.0.0.1:5000
elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open http://127.0.0.1:5000
elif command -v open >/dev/null 2>&1; then
    open http://127.0.0.1:5000
else
    echo "Open browser: http://127.0.0.1:5000"
fi

echo "✅ Novum Ready"
