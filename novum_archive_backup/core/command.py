import importlib
import os
import json

from core.memory import load_memory, add_entry

# ----------------------------
# Command Registry
# ----------------------------

COMMANDS = {}


def register_command(name, func):
    COMMANDS[name] = func


# ----------------------------
# Command Loader (Plugins)
# ----------------------------

def load_commands():
    commands_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "commands")

    print("Loading commands from:", commands_dir)

    for file in os.listdir(commands_dir):
        if file.endswith(".py") and not file.startswith("__"):
            name = file[:-3]

            module = importlib.import_module(f"commands.{name}")

            if hasattr(module, "run"):
                COMMANDS[name] = module.run
                print("Loaded command:", name)


# ----------------------------
# Data File
# ----------------------------

DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "memory.json"
)

# ----------------------------
# Built-in Commands
# ----------------------------

def show_memory(args):
    memory = load_memory() or []

    if memory:
        return ["Memory contents:"] + memory
    else:
        return ["Memory is empty."]


register_command("memory", show_memory)


def search_memory(args):

    if not args:
        return ["Usage: search <term>"]

    term = " ".join(args).lower()
    memory = load_memory() or []

    matches = [m for m in memory if term in m.lower()]

    if matches:
        return [f"Search results for '{term}':"] + matches
    else:
        return [f"No entries found for '{term}'."]


register_command("search", search_memory)


def organize_memory(args):

    memory = load_memory() or []
    organized = sorted(memory, key=lambda x: x.lower())

    if not organized:
        return ["Memory is empty. Nothing to organize."]

    with open(DATA_FILE, "w") as f:
        json.dump(organized, f, indent=2)

    return ["Memory organized alphabetically:"] + organized


register_command("organize", organize_memory)


def systems_check(args):

    return [
        "Running systems check...",
        "All systems operational."
    ]


register_command("systems", systems_check)


def help_command(args):

    output = ["Available commands:"]

    for cmd in sorted(COMMANDS.keys()):
        output.append(f" - {cmd}")

    output.append(" - help")

    return output


register_command("help", help_command)


# ----------------------------
# Command Router
# ----------------------------

def handle_command(text: str):

    text = text.strip()

    if not text:
        return ["No command entered."]

    parts = text.split()
    cmd = parts[0].lower()
    args = parts[1:]

    # Built-in or plugin commands
    if cmd in COMMANDS:

        result = COMMANDS[cmd](args)

        if isinstance(result, list):
            return result

        return [str(result)]

    # Unknown command
    add_entry(f"Unknown command: {text}")

    return [
        f"Command not recognized: '{text}'",
        "Type 'help' for available commands."
    ]
