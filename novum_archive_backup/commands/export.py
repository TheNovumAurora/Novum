import zipfile
import os

def run(args):

    base = os.path.dirname(os.path.dirname(__file__))
    backup = os.path.join(base, "novum_backup.zip")

    with zipfile.ZipFile(backup, "w") as z:
        memory = os.path.join(base, "data", "memory.json")

        if os.path.exists(memory):
            z.write(memory, "data/memory.json")

    return "Novum backup created."
