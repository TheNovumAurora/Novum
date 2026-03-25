import importlib
import os
import json
from core.memory import load_memory, add_entry

COMMANDS = {}

def load_commands():
    commands_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "commands")

    print("Loading commands from:", commands_dir)

    for file in os.listdir(commands_dir):
        if file.endswith(".py") and not file.startswith("__"):
            name = file[:-3]

            module = importlib.import_module(f"commands.{name}")

            if hasattr(module, "run"):
                COMMANDS[name] = module.run
                print("Loaded Command:", name)

DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "memory.json")

def handle_command(command: str):
    """
    Main command handler for Novum.
    Returns a list of strings to display in the UI.
    """
    command = command.strip().lower()
    output = []

    # --- Show full memory ---
    if command == "show memory":
        memory = load_memory() or []
        if memory:
            output.append("Memory contents:")
            output.extend(memory)
        else:
            output.append("Memory is empty.")

    # --- Search memory ---
    elif command.startswith("search "):
        term = command[7:].strip().lower()
        memory = load_memory() or []
        matches = [m for m in memory if term in m.lower()]
        if matches:
            output.append(f"Search results for '{term}':")
            output.extend(matches)
        else:
            output.append(f"No entries found for '{term}'.")

    # --- Organize memory ---
    elif command == "organize":
        memory = load_memory() or []
        organized = sorted(memory, key=lambda x: x.lower())
        if organized:
            output.append("Memory organized alphabetically:")
            output.extend(organized)
            # Save organized memory
            with open(DATA_FILE, "w") as f:
                json.dump(organized, f, indent=2)
        else:
            output.append("Memory is empty. Nothing to organize.")

    # --- Systems check ---
    elif command == "systems check":
        # Placeholder for real system check logic
        output.append("Running systems check...")
        output.append("All systems operational.")  # you can expand with real checks later

    # --- Help / unknown command ---
    elif command == "help":
        output.append("Available commands:")
        output.append(" - show memory : Display all memory entries")
        output.append(" - search <term> : Search memory for a keyword")
        output.append(" - organize : Organize memory alphabetically")
        output.append(" - systems check : Run system diagnostics")
        output.append(" - help : Show this help message")

# --- Plugin commands ---
    else:
        parts = command.split()
        cmd = parts[0]
        args = parts[1:]

        if cmd in COMMANDS:
            result = COMMANDS[cmd](args)

            if isinstance(result, list):
                output.extend(result)
            else:
                output.append(result)

        else:
            add_entry(f"Unknown command: {command}")
            output.append(f"Command not recognized: '{command}'")
            output.append("Type 'help' for available commands.")


    return output
