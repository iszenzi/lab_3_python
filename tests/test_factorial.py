import pytest

from src.math_func import factorial, factorial_recursive


class TestFactorial:
    def test_factorial(self):
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(2) == 2
        assert factorial(3) == 2 * 3
        assert factorial(4) == 2 * 3 * 4
        assert factorial(5) == 2 * 3 * 4 * 5
        assert factorial(6) == 2 * 3 * 4 * 5 * 6
        assert factorial(7) == 2 * 3 * 4 * 5 * 6 * 7
        assert factorial(8) == 2 * 3 * 4 * 5 * 6 * 7 * 8
        assert factorial(9) == 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9
        assert factorial(10) == 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10

    def test_factorial_recursive(self):
        assert factorial_recursive(0) == 1
        assert factorial_recursive(1) == 1
        assert factorial_recursive(2) == 2
        assert factorial_recursive(3) == 2 * 3
        assert factorial_recursive(4) == 2 * 3 * 4
        assert factorial_recursive(5) == 2 * 3 * 4 * 5
        assert factorial_recursive(6) == 2 * 3 * 4 * 5 * 6
        assert factorial_recursive(7) == 2 * 3 * 4 * 5 * 6 * 7
        assert factorial_recursive(8) == 2 * 3 * 4 * 5 * 6 * 7 * 8
        assert factorial_recursive(9) == 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9
        assert factorial_recursive(10) == 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10

    def test_factorial_negative(self):
        with pytest.raises(ValueError) as exc_info:
            factorial(-1)
        assert "Аргумент должен быть целым неотрицательным числом" in str(
            exc_info.value
        )
        assert exc_info.type is ValueError

    def test_factorial_recursive_negative(self):
        with pytest.raises(ValueError) as exc_info:
            factorial_recursive(-1.0)
        assert "Аргумент должен быть целым неотрицательным числом" in str(
            exc_info.value
        )
        assert exc_info.type is ValueError

    def test_factorial_float(self):
        with pytest.raises(ValueError) as exc_info:
            factorial(1.5)
        assert "Аргумент должен быть целым неотрицательным числом" in str(
            exc_info.value
        )
        assert exc_info.type is ValueError

    def test_factorial_recursive_float(self):
        with pytest.raises(ValueError) as exc_info:
            factorial_recursive(1.5)
        assert "Аргумент должен быть целым неотрицательным числом" in str(
            exc_info.value
        )
        assert exc_info.type is ValueError
