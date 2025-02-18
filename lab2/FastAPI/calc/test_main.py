import requests

BASE_URL = "http://127.0.0.1:8000"

def test_add():
    response = requests.get(f"{BASE_URL}/add/", params={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_subtract():
    response = requests.get(f"{BASE_URL}/subtract/", params={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_multiply():
    response = requests.get(f"{BASE_URL}/multiply/", params={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 15}

def test_divide():
    response = requests.get(f"{BASE_URL}/divide/", params={"a": 6, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_divide_by_zero():
    response = requests.get(f"{BASE_URL}/divide/", params={"a": 6, "b": 0})
    assert response.status_code == 400
    assert response.json()["detail"] == "Division by zero is not allowed"