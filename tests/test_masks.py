import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, mask_card_number",
    [
        (1234683378605250, "1234 68** **** 5250"),
        (5000432198764321, "5000 43** **** 4321"),
        (2345678910111213, "2345 67** **** 1213"),
    ],
)
def test_get_mask_card_number_valid(card_number: int, mask_card_number: str) -> None:
    assert get_mask_card_number(card_number) == mask_card_number


@pytest.mark.parametrize("card_number", ["123", 123, "asd", 123456789123456789])
def test_get_mask_card_error(card_number, error_card_number):
    assert get_mask_card_number(card_number) == error_card_number


@pytest.mark.parametrize(
    "account_number, mask_account_number",
    [
        (12345678910111213141, "**3141"),
        (34567891234567891234, "**1234"),
        (98765432198765432198, "**2198"),
    ],
)
def test_get_mask_account_valid(account_number: int, mask_account_number: str) -> None:
    assert get_mask_account(account_number) == mask_account_number


@pytest.mark.parametrize(
    "account_number", ["123", 123, "asd", 123456789123456789102, [1, 2, 3]]
)
def test_get_mask_account_error(account_number, error_account_number):
    assert get_mask_account(account_number) == error_account_number
