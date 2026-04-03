import json
import os

MEMORY_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "memory.json")


def load_memory():
    """Load memory from JSON file. Returns a list of entries."""
    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except json.JSONDecodeError:
        return []


def add_entry(entry: str):
    """Add a new entry to memory, avoiding duplicates."""
    memory = load_memory()
    memory.append(entry)
    # Optional: remove exact duplicates
    memory = list(dict.fromkeys(memory))
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)
