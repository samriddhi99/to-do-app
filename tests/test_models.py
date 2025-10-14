import pytest
from src.models import Todo, load_todos, save_todos
import os
import json

def test_todo_creation():
    t = Todo("Test")
    assert t.title == "Test"
    assert t.status == "pending"

def test_save_and_load(tmp_path):
    file_path = tmp_path / "todos.json"
    todo = Todo("Task1")
    data = [{"title": todo.title, "status": todo.status}]
    with open(file_path, "w") as f:
        json.dump(data, f)
    with open(file_path, "r") as f:
        loaded = json.load(f)
    assert loaded[0]["title"] == "Task1"
