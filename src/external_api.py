import os

import requests
from dotenv import load_dotenv
from requests import Response

load_dotenv()

API_KEY_EXCHANGE: str | None = os.getenv("API_KEY_EXCHANGE")


def sum_transaction_in_rub(transaction: dict) -> float:
    """
    Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют и
    конвертации суммы операции в рубли. Для конвертации валюты использует Exchange Rates Data API:
    https://apilayer.com/exchangerates_data-api.
    :param transaction: - словарь с транзакцией
    :return: - сумма в рублях float
    """

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        amount_transaction: float = transaction["operationAmount"]["amount"]
    else:
        url: str = "https://api.apilayer.com/exchangerates_data/convert"
        payload: dict = {
            "amount": transaction["operationAmount"]["amount"],
            "from": transaction["operationAmount"]["currency"]["code"],
            "to": "RUB",
        }
        headers: dict = {"apikey": API_KEY_EXCHANGE}

        try:
            response: Response = requests.get(url, headers=headers, params=payload)
            print(response.json())
            result: dict = response.json()

            amount_transaction: float = result["result"]

        except Exception as e:
            print(f"Непредвиденная ошибка: {str(e)}")
            raise Exception("API error") from e
    return amount_transaction
