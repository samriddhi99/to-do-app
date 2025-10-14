import json
from src.constants import TODO_FILE, VALID_STATUSES
from src.exceptions import TodoError

class Todo:
    def __init__(self, title, status="pending"):
        if status not in VALID_STATUSES:
            raise TodoError(f"Invalid status: {status}")
        self.title = title
        self.status = status

def load_todos():
    try:
        with open(TODO_FILE, "r") as f:
            data = json.load(f)
        return [Todo(**item) for item in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise TodoError("Failed to parse todos file")

def save_todos(todos):
    data = [{"title": t.title, "status": t.status} for t in todos]
    with open(TODO_FILE, "w") as f:
        json.dump(data, f, indent=2)
