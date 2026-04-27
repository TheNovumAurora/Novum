#!/usr/bin/env bash

echo "🚀 Installing Novum..."

INSTALL_DIR="$HOME/Novum"

install_deps() {
    if command -v pkg >/dev/null 2>&1; then
        echo "📱 Termux detected"
        pkg update -y || true
        pkg install -y python git curl || true
    elif command -v apt >/dev/null 2>&1; then
        echo "🐧 Linux detected"
        sudo apt update -y
        sudo apt install -y python3 python3-pip git curl
    elif command -v brew >/dev/null 2>&1; then
        echo "🍎 Mac detected"
        brew install python git curl
    else
        echo "⚠️ Unknown system. Please install python3, pip, git, and curl manually."
    fi
}

install_deps

if [ -d "$INSTALL_DIR/.git" ]; then
    echo "🔄 Updating Novum..."
    cd "$INSTALL_DIR" || exit 1
    git pull
else
    echo "📦 Cloning Novum..."
    git clone https://github.com/TheNovumAurora/novum.git "$INSTALL_DIR"
    cd "$INSTALL_DIR" || exit 1
fi

echo "📦 Installing Python dependencies..."
if command -v pip3 >/dev/null 2>&1; then
    pip3 install -r core/requirements.txt
else
    python3 -m pip install -r core/requirements.txt
fi

mkdir -p "$HOME/.local/bin"

cat > "$HOME/.local/bin/novum" << 'EOF'
#!/usr/bin/env bash

echo "🧠 Starting Novum..."

cd "$HOME/Novum" || exit 1

pkill -f "core.interface.web" 2>/dev/null

python3 -m core.interface.web &

sleep 2

if command -v termux-open-url >/dev/null 2>&1; then
    termux-open-url http://127.0.0.1:5000
elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open http://127.0.0.1:5000
elif command -v open >/dev/null 2>&1; then
    open http://127.0.0.1:5000
else
    echo "Open browser: http://127.0.0.1:5000"
fi
EOF

chmod +x "$HOME/.local/bin/novum"

case ":$PATH:" in
    *":$HOME/.local/bin:"*) ;;
    *)
        if [ -f "$HOME/.bashrc" ]; then
            echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
        fi
        if [ -f "$HOME/.zshrc" ]; then
            echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.zshrc"
        fi
        export PATH="$HOME/.local/bin:$PATH"
        ;;
esac

echo "✅ Novum installed!"
echo "👉 Run: novum"
