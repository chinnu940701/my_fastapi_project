from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"email": "test@example.com"})
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_create_item():
    response = client.post("/users/1/items/", json={"title": "Sample Item", "description": "Sample description"})
    assert response.status_code == 200
    assert response.json()["title"] == "Sample Item"

def test_get_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert len(response.json()) > 0

