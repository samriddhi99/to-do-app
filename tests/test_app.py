import pytest
from src.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_empty_todos(client):
    rv = client.get("/todos")
    assert rv.status_code == 200
    assert rv.get_json() == []

def test_create_todo(client):
    rv = client.post("/todos", json={"title": "Test Task"})
    assert rv.status_code == 201
    assert rv.get_json()["title"] == "Test Task"
