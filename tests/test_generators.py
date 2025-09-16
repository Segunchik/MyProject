from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(transactions_list: list) -> None:
    result = list(filter_by_currency(transactions_list, "USD"))
    assert len(result) == 3
    for transaction in result:
        assert transaction["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_rub(transactions_list: list) -> None:
    result = list(filter_by_currency(transactions_list, "RUB"))
    assert len(result) == 2
    for transaction in result:
        assert transaction["operationAmount"]["currency"]["code"] == "RUB"


def test_filter_by_currency_wrong(transactions_list: list) -> None:
    result = list(filter_by_currency(transactions_list, "EUR"))
    assert len(result) == 0
    assert result == []


def test_filter_by_currency_empty() -> None:
    result = list(filter_by_currency([], "USD"))
    assert len(result) == 0
    assert result == []


def test_transaction_descriptions(transactions_list: list, descriptions_all: list) -> None:
    assert list(transaction_descriptions(transactions_list)) == descriptions_all


def test_descriptions_empty_list_transactions() -> None:
    result = list(transaction_descriptions([]))
    assert result == []


def test_card_number_generator(generated_card_list: list) -> None:
    assert list(card_number_generator(1, 5)) == generated_card_list
