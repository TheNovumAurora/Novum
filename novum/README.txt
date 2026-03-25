==========================
Novum Aurora - Quick Start
==========================

Welcome to Novum Aurora! This guide will get you up and running on Termux with **one command**.

1. **Ensure Termux is Installed**
   - Install Termux from the Play Store or F-Droid.

2. **Unzip Novum**
   - Extract this folder to your home directory: ~/novum
   - Example:
       unzip novum_full_snapshot.zip -d $HOME

3. **Install Python & Dependencies**
   - Open Termux and run:
       pkg install -y python
       pip install --upgrade pip
       pip install -r ~/novum/requirements.txt

4. **One-Command Launch**
   - You can start Novum Aurora with a single command:
       novum
   - This will:
       * Start the Flask server
       * Open the UI in your default browser
       * Keep everything ready to use

5. **Using Novum**
   - Command Console: type commands here.
   - Activity Feed: shows logs of your actions.
   - Example commands:
       - show memory
       - search <term>
       - organize
       - systems check
       - remember <text>
       - help
   - Add your own commands in the `commands/` folder.

6. **Tips**
   - Ensure Termux has permission to open URLs (required for auto-browser).  
   - Keep the Novum folder in `$HOME/novum` to avoid path issues.  
   - To update Novum, overwrite the folder with a newer zip.

7. **Troubleshooting**
   - If the UI doesn’t open, check that Python and Flask are installed:
       pip install flask
   - Make sure the `novum` command is executable:
       chmod +x ~/novum/novum
