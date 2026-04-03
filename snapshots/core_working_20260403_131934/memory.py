import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEMORY_FILE = os.path.join(BASE_DIR, "data", "memory.json")


def ensure_memory():
    """Ensure memory directory and file exist."""
    os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)

    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump([], f, indent=2)


def load_memory():
    """Load memory from JSON file. Returns a list of entries."""
    ensure_memory()

    try:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except json.JSONDecodeError:
        return []


def save_memory(memory):
    """Save memory list to file."""
    ensure_memory()

    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def add_entry(entry: str):
    """Add a new entry to memory, avoiding duplicates."""
    memory = load_memory()
    memory.append(entry)

    # Remove duplicates while preserving order
    memory = list(dict.fromkeys(memory))

    save_memory(memory)
