def factorial(n: int) -> int:
    if n < 0 or type(n) is not int:
        raise ValueError("Число должно быть целым неотрицательным")
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    if n < 0 or type(n) is not int:
        raise ValueError("Число должно быть целым неотрицательным")
    if n == 0:
        return 1
    return factorial_recursive(n - 1) * n


def fibo(n: int) -> int:
    if n < 0 or type(n) is not int:
        raise ValueError("Число должно быть целым неотрицательным")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, b + a
    return b


def fibo_recursive(n: int) -> int:
    if n < 0 or type(n) is not int:
        raise ValueError("Число должно быть целым неотрицательным")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)
