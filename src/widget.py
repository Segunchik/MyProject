from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа
    """
    parts_of_account = account_card.split()

    if parts_of_account[0].lower() == "счет":
        parts_of_account[-1] = get_mask_account(int(parts_of_account[-1]))
        return ' '.join(parts_of_account)
    else:
        parts_of_account[-1] = get_mask_card_number(int(parts_of_account[-1]))
        return ' '.join(parts_of_account)


def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой из формата "2024-03-11T02:26:18.671407" в формат ДД.ММ.ГГГГ.
    """

    dt_obj = datetime.fromisoformat(date_string)
    return dt_obj.strftime("%d.%m.%Y")
# print(mask_account_card("Счет 73654108430135874305"))
# print(mask_account_card("Visa Platinum 7000792289606361"))
# print(get_date("2024-03-11T02:26:18.671407"))
