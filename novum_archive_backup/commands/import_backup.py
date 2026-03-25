import zipfile
import os

def run(args):

    base = os.path.dirname(os.path.dirname(__file__))
    backup = os.path.join(base, "novum_backup.zip")

    if not os.path.exists(backup):
        return "Backup file not found."

    with zipfile.ZipFile(backup, "r") as z:
        z.extractall(base)

    return "Backup restored."
