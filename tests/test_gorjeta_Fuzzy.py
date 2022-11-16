from unittest.mock import Mock
from unittest import mock
from unittest.mock import patch, MagicMock
import pytest

from fastapi.testclient import TestClient
import httpx

from gorjeta_Fuzzy import gorjeta
from app import home
from app import app

client = TestClient(app)

def test_gorjeta77():
    info = gorjeta(7, 7)  #{"Gorjeta": 15.777777777777775}
    assert info == 15.777777777777775

@pytest.mark.parametrize("_input, expected", [([7, 7], {'gorjeta': 15.777777777777775}), ([6,3], {'gorjeta': 8.516638465877042})])
def test_mockGorjeta(_input, expected):
    assert home(_input[0], _input[1]) == expected

@patch('app.home')
def test_mockG(mock_post):
    mock_post.return_value = {"gorjeta": 15.777777777777775}
    assert home(7,7) == {"gorjeta": 15.777777777777775}

@patch('app.home')
def test_mock2(mock_resquests):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"gorjeta": 15.777777777777775}

    mock_resquests.get.return_value = mock_response
    assert home(7, 7) == {"gorjeta": 15.777777777777775}

def test_api():
    response = client.post('http://127.0.0.1:8000/gorjeta?servico=7&qualidade=7')
    print(response)
    assert response.json() == {"gorjeta": 15.777777777777775}
    assert response.status_code == 200


