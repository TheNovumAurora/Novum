import os
from flask import Flask, render_template, request, jsonify

from core.command import handle_command, load_commands
from core.memory import add_entry

load_commands()

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), "templates")
)

GREETINGS = [
    "What ideas do you have today?",
    "Hello, Ty.",
    "Welcome back.",
    "Good to see you.",
    "Ready to log something?"
]


@app.route("/", methods=["GET"])
def home():
    return render_template("console.html")


@app.route("/command", methods=["POST"])
def command_api():
    data = request.get_json(silent=True) or {}
    command = data.get("command", "").strip()

    if not command:
        return jsonify({"output": ["No command entered."]})

    result = handle_command(command)

    if result is not None:
        add_entry(command)

    if not isinstance(result, list):
        result = [str(result)]

    return jsonify({"output": result})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
