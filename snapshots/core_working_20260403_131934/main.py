import webbrowser
import threading
from interface.web import app
from core.command import load_commands

def open_browser():
    import time
    time.sleep(1)  # Wait for Flask to start
    webbrowser.open("http://127.0.0.1:5000/")

if __name__ == "__main__":
    load_commands()
    threading.Thread(target=open_browser).start()
    app.run(debug=True, host="0.0.0.0", port=5000)
