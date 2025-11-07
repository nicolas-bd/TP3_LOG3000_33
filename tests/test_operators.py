from operators import add, subtract, multiply, divide

"""Tests de cas extremes pour add, subtract, multiply et divide."""

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-2, -3) == -5


def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(2, 5) == -3
    assert subtract(0, 0) == 0
    assert subtract(5, 5) == 0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(3, 2) == 6
    assert multiply(3, 0) == 0
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6


def test_divide():
    assert divide(12, 5) == 2.4
    assert divide(3, 2) == 1.5
    assert divide(0, 5) == 0
    assert divide(-6, 2) == -3
