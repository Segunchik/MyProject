from unittest.mock import patch, MagicMock
import requests

from src.external_api import sum_transaction_in_rub

# Пример тестовой транзакции
TEST_TRANSACTION_RUB = {
    "operationAmount": {
        "amount": 1000.0,
        "currency": {"code": "RUB"}
    }
}

TEST_TRANSACTION_USD = {
    "operationAmount": {
        "amount": 100.0,
        "currency": {"code": "USD"}
    }
}

TEST_TRANSACTION_EUR = {
    "operationAmount": {
        "amount": 100.0,
        "currency": {"code": "EUR"}
    }
}


def test_rub_transaction():
    result = sum_transaction_in_rub(TEST_TRANSACTION_RUB)
    assert result == 1000.0


@patch('requests.get')
def test_usd_transaction(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": 12000.0}
    mock_get.return_value = mock_response

    result = sum_transaction_in_rub(TEST_TRANSACTION_USD)
    assert result == 12000.0

    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": "API_KEY_EXCHANGE"},
        params={
            "amount": 100.0,
            "from": "USD",
            "to": "RUB"
        }
    )


@patch('requests.get')
def test_eur_transaction(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": 13000.0}
    mock_get.return_value = mock_response

    result = sum_transaction_in_rub(TEST_TRANSACTION_EUR)
    assert result == 13000.0, f"Ожидалось 13000.0, получено {result}"

    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert",
        headers={"apikey": "API_KEY_EXCHANGE"},
        params={
            "amount": 100.0,
            "from": "EUR",
            "to": "RUB"
        }
    )


@patch('requests.get')
def test_api_error(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException("API error")

    try:
        sum_transaction_in_rub(TEST_TRANSACTION_USD)
    except Exception as e:
        assert str(e) == "API error"


@patch('requests.get')
def test_invalid_response(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = {"error": "Invalid request"}
    mock_get.return_value = mock_response

    try:
        sum_transaction_in_rub(TEST_TRANSACTION_USD)
    except Exception as e:
        assert str(e) == "API error"
