from core.command import COMMANDS

def run(args):
    output = ["Available commands:"]

    for cmd in sorted(COMMANDS.keys()):
        output.append(f" - {cmd}")

    return output
