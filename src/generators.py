from typing import Any, Generator, Iterator


def filter_by_currency(transactions: list, currency: str = "USD") -> Iterator[dict]:
    """
    Функция принимает на вход список словарей, представляющих транзакции
    и отфильтровывает по ключу currency
    Входные параметры:
    transactions(list) - список словарей с транзакциями.
    currency(str) - код валюты, по умолчанию USD

    Возвращает отфильтрованный список
    """
    return (x for x in transactions if x["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(transactions: list) -> list:
    """
    Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, Any, None]:
    """
    Функция генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где
    X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    """
    for num in range(start, end + 1):
        card = f"{num:016d}"  # 16-значное число с ведущими нулями
        yield f"{card[:4]} {card[4:8]} {card[8:12]} {card[12:]}"
