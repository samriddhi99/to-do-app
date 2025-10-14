from flask import Flask, jsonify, request
from src.utils import add_todo, mark_done, load_todos
from src.exceptions import TodoError

app = Flask(__name__)

@app.route("/todos", methods=["GET"])
def get_todos():
    todos = load_todos()
    return jsonify([{"title": t.title, "status": t.status} for t in todos])

@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()
    try:
        todo = add_todo(data["title"])
        return jsonify({"title": todo.title, "status": todo.status}), 201
    except TodoError as e:
        return jsonify({"error": str(e)}), 400

@app.route("/todos/<title>/done", methods=["POST"])
def complete_todo(title):
    try:
        todo = mark_done(title)
        return jsonify({"title": todo.title, "status": todo.status})
    except TodoError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
