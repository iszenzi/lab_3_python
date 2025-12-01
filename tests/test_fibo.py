import pytest
from src.math_func import fibo, fibo_recursive


class TestFibo:
    def test_fibo(self):
        assert fibo(0) == 0
        assert fibo(1) == 1
        assert fibo(2) == 1
        assert fibo(3) == 1 + 1
        assert fibo(4) == 1 + 2
        assert fibo(5) == 2 + 3
        assert fibo(6) == 3 + 5
        assert fibo(7) == 5 + 8
        assert fibo(8) == 8 + 13
        assert fibo(9) == 13 + 21
        assert fibo(10) == 21 + 34

    def test_fibo_recursive(self):
        assert fibo_recursive(0) == 0
        assert fibo_recursive(1) == 1
        assert fibo_recursive(2) == 1
        assert fibo_recursive(3) == 1 + 1
        assert fibo_recursive(4) == 1 + 2
        assert fibo_recursive(5) == 2 + 3
        assert fibo_recursive(6) == 3 + 5
        assert fibo_recursive(7) == 5 + 8
        assert fibo_recursive(8) == 8 + 13
        assert fibo_recursive(9) == 13 + 21
        assert fibo_recursive(10) == 21 + 34

    def test_fibo_negative_raises(self):
        with pytest.raises(ValueError) as exc_info:
            fibo(-1)
        assert "Аргумент должен быть целым неотрицательным числом" in str(
            exc_info.value
        )
        assert exc_info.type is ValueError

    def test_fibo_recursive_negative(self):
        with pytest.raises(ValueError) as exc_info:
            fibo_recursive(-1.0)
        assert "Аргумент должен быть целым неотрицательным числом" in str(
            exc_info.value
        )
        assert exc_info.type is ValueError

    def test_fibo_float(self):
        with pytest.raises(ValueError) as exc_info:
            fibo(1.5)
        assert "Аргумент должен быть целым неотрицательным числом" in str(
            exc_info.value
        )
        assert exc_info.type is ValueError

    def test_fibo_recursive_float(self):
        with pytest.raises(ValueError) as exc_info:
            fibo_recursive(1.5)
        assert "Аргумент должен быть целым неотрицательным числом" in str(
            exc_info.value
        )
        assert exc_info.type is ValueError
