import random
import os
import sys
from flask import Flask, render_template, request, jsonify
from core.command import handle_command

# Ensure Python sees core modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.memory import load_memory, add_entry
from core.command import handle_command, load_commands

load_commands()

# Explicitly tell Flask where templates are
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "templates"))

GREETINGS = [
    "What ideas do you have today?",
    "Hello, Ty.",
    "Welcome back.",
    "Good to see you.",
    "Ready to log something?"
]

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        output_lines = []

        if text:
        # Handle the command first
            result = handle_command(text)

            if result is not None:
            # Only save valid command outputs
                add_entry(text)
                if isinstance(result, list):
                    output_lines.extend(result)
                else:
                    output_lines.append(result)
            else:
            # Unknown commands are shown but NOT saved
                output_lines.append(f"Unknown command: {text}")
        output = "\n".join(output_lines) if output_lines else ""
    return render_template("console.html")

@app.route("/command", methods=["POST"])
def command_api():
    data = request.get_json()
    print("Received:", data)
    command = data.get("command", "").strip()
    result = handle_command(command)
    print("Result:", result)
    return jsonify({"output": result})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
