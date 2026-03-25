import json
import os
from datetime import datetime

MEMORY_FILE = os.path.join(os.path.expanduser("~"), "core_system", "novum", "memory.json")

def load_memory():
    """Load memory from JSON file; fallback to empty list if missing or invalid."""
    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r") as f:
            data = f.read().strip()
            if not data:
                return []
            mem = json.loads(data)
            if isinstance(mem, list):
                return mem
            else:
                return []
    except json.JSONDecodeError:
        return []

def save_memory(memory):
    """Save memory list to JSON file."""
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def add_entry(text):
    """Add a new entry to memory and save it."""
    memory = load_memory()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"{timestamp} | {text}"
    memory.append(entry)
    save_memory(memory)
    return {"entry": entry, "tags": []}
