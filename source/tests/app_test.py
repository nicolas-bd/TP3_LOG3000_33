# Needed to set the system path to make it work
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from source.app import app, calculate


# -------------------
# Tests for calculate
# -------------------

def test_calculate_add():
    """
    adding two valid operands should
    return the correct response as a number.
    """
    assert calculate("2+3") == 5
    #inserting arbitrary spaces
    assert calculate("10 + 20") == 30


def test_calculate_subtract():
    """
    subtracting two valid operands should
    return the correct response as a number.
    """
    assert calculate("5-3") == 2
    # inserting arbitrary spaces
    assert calculate("10 - 4") == 6


def test_calculate_multiply():
    """
    multiplying two valid operands should
    return the correct response as a number.
    """
    assert calculate("2*3") == 6
    # inserting arbitrary spaces
    assert calculate("5 * 5") == 25


def test_calculate_divide():
    """
    dividing two valid operands should
    return the correct response as a number.
    """
    assert calculate("6/3") == 2
    # inserting arbitrary spaces
    assert calculate("10 / 4") == 2.5


def test_calculate_invalid_expression():
    """
    Trying to calculate an invalid expression should
    return a value error.
    """
    # empty expression calculation
    with pytest.raises(ValueError):
        calculate("")
    # multiple operator calculation
    with pytest.raises(ValueError):
        calculate("2+3-1")
    with pytest.raises(ValueError):
        calculate("2+3+1")
    # operator at start/end calculation
    with pytest.raises(ValueError):
        calculate("+5")
    with pytest.raises(ValueError):
        calculate("5-")
    # invalid operand calculation
    with pytest.raises(ValueError):
        calculate("a+5")
    with pytest.raises(ValueError):
        calculate("5+a")
    with pytest.raises(ValueError):
        calculate("a+b")


# -------------------
# Tests for Flask app
# -------------------

@pytest.fixture
def client():
    # this will stand for our client for these tests
    with app.test_client() as client:
        yield client


def test_index_get(client):
    # GET request returns 200
    response = client.get('/')
    assert response.status_code == 200


def test_index_post_valid(client):
    # POST request with valid expression displays the correct result
    response = client.post('/', data={'display': '3+4'})
    assert response.status_code == 200
    assert b"7" in response.data


def test_index_post_invalid(client):
    # POST request with invalid expression displays the error
    response = client.post('/', data={'display': '3++4'})
    assert response.status_code == 200
    assert b"Error:" in response.data
