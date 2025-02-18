import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Тест для последовательности Фибоначчи
def test_fibonacci():
    response = client.get("/number?n=10&sequence=fibonacci")
    assert response.status_code == 200
    assert response.json() == {"number": 55}  # 10-е число Фибоначчи

# Тест для последовательности простых чисел
def test_prime():
    response = client.get("/number?n=7&sequence=prime")
    assert response.status_code == 200
    assert response.json() == {"number": 17}  # 7-е простое число

# Тест для проверки некорректной последовательности
def test_invalid_sequence():
    response = client.get("/number?n=10&sequence=invalid")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid sequence type"}

# Тест для проверки отрицательного значения n
def test_negative_n():
    response = client.get("/number?n=-1&sequence=fibonacci")
    assert response.status_code == 400
    assert response.json() == {"detail": "n must be a non-negative integer"}

# Тест для проверки n = 0
def test_zero_n():
    response = client.get("/number?n=0&sequence=fibonacci")
    assert response.status_code == 200
    assert response.json() == {"number": 0}  # 0-е число Фибоначчи