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
    assert calculate("2+3") == 5
    assert calculate("10 + 20") == 30

def test_calculate_subtract():
    assert calculate("5-3") == 2
    assert calculate("10 - 4") == 6

def test_calculate_multiply():
    assert calculate("2*3") == 6
    assert calculate("5 * 5") == 25

def test_calculate_divide():
    assert calculate("6/3") == 2
    assert calculate("10 / 4") == 2.5

def test_calculate_invalid_expression():
    # empty string
    with pytest.raises(ValueError):
        calculate("")
    # multiple operators
    with pytest.raises(ValueError):
        calculate("2+3-1")
    # operator at start/end
    with pytest.raises(ValueError):
        calculate("+5")
    with pytest.raises(ValueError):
        calculate("5-")
    # invalid operands
    with pytest.raises(ValueError):
        calculate("a+5")

# -------------------
# Tests for Flask app
# -------------------

@pytest.fixture
def client():
    # Create a test client
    with app.test_client() as client:
        yield client

def test_index_get(client):
    # GET request returns 200
    response = client.get('/')
    assert response.status_code == 200
    assert b"result" in response.data  # the template includes 'result'

def test_index_post_valid(client):
    # POST request with valid expression
    response = client.post('/', data={'display': '3+4'})
    assert response.status_code == 200
    assert b"7" in response.data

def test_index_post_invalid(client):
    # POST request with invalid expression
    response = client.post('/', data={'display': '3++4'})
    assert response.status_code == 200
    assert b"Error:" in response.data