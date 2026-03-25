# commands/remember.py
from core.memory import add_entry

def run(args):
    if not args:
        return "Usage: remember <idea>"

    idea = " ".join(args)
    add_entry(f"Remembered: {idea}")
    return f"I've stored your idea: '{idea}'"
