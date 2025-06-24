import json
from collections import deque
from pathlib import Path

HISTORY_FILE = Path(".ai_history.json")
MAX_HISTORY = 5

def load_history():
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r") as f:
            return deque(json.load(f), maxlen=MAX_HISTORY)
    return deque(maxlen=MAX_HISTORY)

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(list(history), f, indent=2)

_history = load_history()

def add_to_history(user_msg, ai_response):
    _history.append((user_msg, ai_response))
    save_history(_history)

def get_history():
    return list(_history)
