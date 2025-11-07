import pytest
from bs4 import BeautifulSoup

"""Fixture simple qui retourne un serveur de test Flask."""
@pytest.fixture
def client():
    from app import app as flask_app
    return flask_app.test_client()


"""
Tests pour l'interface utilisateur du serveur Flask.
Vérifie la présence des boutons de la calculatrice dans le HTML rendu.
"""
def test_button_present(client):
    rv = client.get('/')
    html = rv.data.decode('utf-8')
    assert '<button' in html

    
def test_button_1_present(client):
    rv = client.get('/')
    html = rv.data.decode('utf-8')
    assert '>1<' in html


def test_button_2_present(client):
    rv = client.get('/')
    html = rv.data.decode('utf-8')
    assert '>2<' in html


def test_button_3_present(client):
    rv = client.get('/')
    html = rv.data.decode('utf-8')
    assert '>3<' in html


def test_button_plus_present(client):
    rv = client.get('/')
    html = rv.data.decode('utf-8')    
    assert '>+<' in html


def test_button_4_present(client):
    rv = client.get('/')
    html = rv.data.decode('utf-8')
    assert '>4<' in html


def test_button_5_present(client):
    rv = client.get('/')
    html = rv.data.decode('utf-8')
    assert '>5<' in html


def test_button_6_present(client):
    rv = client.get('/')
    html = rv.data.decode('utf-8')
    assert '>6<' in html


def test_button_minus_present(client):
    rv = client.get('/')
    html = rv.data.decode('utf-8')
    assert '>-<' in html
    

def test_button_7_present(client):
    rv = client.get('/')
    html = rv.data.decode('utf-8')
    assert '>7<' in html


def test_button_8_present(client):
    rv = client.get('/')
    html = rv.data.decode('utf-8')
    assert '>8<' in html


def test_button_9_present(client):
    rv = client.get('/')
    html = rv.data.decode('utf-8')
    assert '>9<' in html


def test_button_mul_present(client):
    rv = client.get('/')
    html = rv.data.decode('utf-8')
    assert '>*<' in html


def test_button_0_present(client):
    rv = client.get('/')
    html = rv.data.decode('utf-8')
    assert '>0<' in html


def test_button_C_present(client):
    rv = client.get('/')
    html = rv.data.decode('utf-8')
    assert '>C<' in html


def test_button_eq_present(client):
    rv = client.get('/')
    html = rv.data.decode('utf-8')
    assert '>=<' in html


def test_button_div_present(client):
    rv = client.get('/')
    html = rv.data.decode('utf-8')
    assert '>/<' in html


    # S'assure qu'aucun caractère de remplacement Unicode n'est présent
    assert '\ufffd' not in html  # \ufffd is the Unicode replacement character

    # Pas de boutons vides
    soup = BeautifulSoup(html, 'html.parser')
    for btn in soup.select('button'):
        text = btn.get_text(strip=True)
        assert text != '', f'Empty button found: {btn}'
