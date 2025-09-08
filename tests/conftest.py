import pytest


@pytest.fixture
def error_card_number() -> str:
    return "Введен некорректный номер карты"


@pytest.fixture
def error_account_number() -> str:
    return "Введен некорректный номер счета"
