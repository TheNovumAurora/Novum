#!/data/data/com.termux/files/usr/bin/bash
# install_novum.sh
# Termux-friendly installer for Novum Aurora
# Ensures dependencies, cleans cache, and sets up a simple launch command

# Move to Novum folder
cd "$(dirname "$0")" || exit 1

echo "[Novum] Setting up your environment..."

# --- 1. Update and install Python & pip if missing ---
echo "[Novum] Checking Python installation..."
pkg install -y python || { echo "Python install failed"; exit 1; }
pip install --upgrade pip

# --- 2. Install required Python packages ---
if [ -f "requirements.txt" ]; then
    echo "[Novum] Installing Python dependencies..."
    pip install -r requirements.txt
fi

# --- 3. Clean __pycache__ directories ---
echo "[Novum] Cleaning temporary files..."
find . -type d -name "__pycache__" -exec rm -rf {} +

# --- 4. Ensure all folders are proper Python packages ---
echo "[Novum] Ensuring package structure..."
find . -type d -exec touch {}/__init__.py \; 2>/dev/null

# --- 5. Make launch scripts executable ---
echo "[Novum] Setting execute permissions..."
chmod +x launch_novum.sh
chmod +x run_web.sh
chmod +x main.py

# --- 6. Add 'novum' command shortcut ---
NOVUM_BIN="$PREFIX/bin/novum"
echo "[Novum] Creating command shortcut at $NOVUM_BIN"

#
