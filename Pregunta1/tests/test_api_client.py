import pytest
from unittest.mock import patch, create_autospec, Mock
import requests


# patch que permite reemplazar el requests.get con un mock
# para simular una respuesta de laAPI sin tener que hacer un request real
@patch('requests.get')
def test_api_client(mock_get):
    # crear mock de la respuesta de requests.get
    mock_respuesta = create_autospec(requests.Response)
    mock_respuesta.status_code = 200
    mock_respuesta.json.return_value = {"key": "value"}
    mock_get.return_value = mock_respuesta
    # llamando a la API simulada
    respuesta = requests.get("https://api.example.com/data")
    # para verificar que la respuesta es la que se espera
    assert respuesta.status_code == 200
    assert respuesta.json() == {"key": "value"}
    mock_get.assert_called_with("https://api.example.com/data")
