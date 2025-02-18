from fastapi import FastAPI, HTTPException
from math import isqrt

app = FastAPI()

# Функция для проверки, является ли число простым
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

# Функция для вычисления n-го числа Фибоначчи
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Функция для нахождения n-го простого числа
def nth_prime(n: int) -> int:
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes[-1]

# Основной эндпоинт
@app.get("/number")
def get_number(n: int, sequence: str):
    if sequence == "fibonacci":
        if n < 0:
            raise HTTPException(status_code=400, detail="n must be a non-negative integer")
        return {"number": fibonacci(n)}
    elif sequence == "prime":
        if n <= 0:
            raise HTTPException(status_code=400, detail="n must be a positive integer")
        return {"number": nth_prime(n)}  # Возвращаем n-е простое число
    else:
        raise HTTPException(status_code=400, detail="Invalid sequence type")