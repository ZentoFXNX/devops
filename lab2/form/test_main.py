from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_uppercase():
    response = client.post("/format", json={"text": "hello world", "operation": "upper"})
    assert response.status_code == 200
    assert response.json() == {"formatted_text": "HELLO WORLD"}

def test_lowercase():
    response = client.post("/format", json={"text": "HELLO WORLD", "operation": "lower"})
    assert response.status_code == 200
    assert response.json() == {"formatted_text": "hello world"}

def test_capitalize():
    response = client.post("/format", json={"text": "hello world", "operation": "capitalize"})
    assert response.status_code == 200
    assert response.json() == {"formatted_text": "Hello world"}

def test_title_case():
    response = client.post("/format", json={"text": "hello world", "operation": "title"})
    assert response.status_code == 200
    assert response.json() == {"formatted_text": "Hello World"}

def test_invalid_operation():
    response = client.post("/format", json={"text": "hello world", "operation": "invalid"})
    assert response.status_code == 200
    assert response.json() == {"error": "Invalid operation"}
