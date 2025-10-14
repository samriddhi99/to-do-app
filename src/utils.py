from src.models import load_todos, save_todos, Todo
from src.exceptions import TodoError

def add_todo(title):
    todos = load_todos()
    todo = Todo(title)
    todos.append(todo)
    save_todos(todos)
    return todo

def mark_done(title):
    todos = load_todos()
    for todo in todos:
        if todo.title == title:
            todo.status = "done"
            save_todos(todos)
            return todo
    raise TodoError(f"Todo '{title}' not found")
