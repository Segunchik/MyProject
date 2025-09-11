import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card, masked",
    [
        ("Visa Platinum 1234567891234567", "Visa Platinum 1234 56** **** 4567"),
        ("Maestro 1234567891234567", "Maestro 1234 56** **** 4567"),
        ("Счет 98765432198765432198", "Счет **2198"),
    ],
)
def test_mask_account_card_valid(account_card: str, masked: str) -> None:
    assert mask_account_card(account_card) == masked


@pytest.mark.parametrize(
    "account_number", ["Счет 123", 123, "asd 1", 123456789123456789]
)
def test_mask_account_error(account_number, error_account):
    assert mask_account_card(account_number) == error_account


@pytest.mark.parametrize(
    "date, format_date",
    [
        ("2023-02-18T15:36:18.123456", "18.02.2023"),
        ("2015-12-13T01:53:59.654321", "13.12.2015"),
        ("2025-01-01T00:00:00", "01.01.2025"),
    ],
)
def test_get_date(date, format_date):
    assert get_date(date) == format_date
