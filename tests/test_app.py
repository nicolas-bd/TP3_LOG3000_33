from app import calculate

"""Tests pour la fonction calculate dans app.py."""

"""Tests d'espaces additionnels"""
def test_calculate_add():
    assert calculate("1+2") == 3
    assert calculate(" 3 + 4 ") == 7


"""Tests de diff/érents opérateurs"""
def test_calculate_subtract():
    assert calculate("5-5") == 0


def test_calculate_multiply():
    assert calculate("2*3") == 6


def test_calculate_divide():
    assert calculate("6/3") == 2


"""Tests d'entrées invalides"""
def test_invalid_empty():
    with pytest.raises(ValueError):
        calculate("")


def test_invalid_multiple_operators():
    with pytest.raises(ValueError):
        calculate("1+2-3")


def test_invalid_operator_position():
    with pytest.raises(ValueError):
        calculate("+12")
    with pytest.raises(ValueError):
        calculate("12+")


def test_non_numeric_operands():
    with pytest.raises(ValueError):
        calculate("a+b")
