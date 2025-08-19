from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа
    """
    parts_of_account = account_card.split()
 #   parts_of_account[-1] = '324685311'
    print(parts_of_account)

    if parts_of_account[0].lower() == "счет":
        parts_of_account[-1] = get_mask_account(int(parts_of_account[-1]))
        return ' '.join(parts_of_account)
    else:
        parts_of_account[-1] = get_mask_card_number(int(parts_of_account[-1]))
        return ' '.join(parts_of_account)

#        print(parts_of_account[-1])
 #   number_acc = ''.join(filter(str.isdigit, account_card)
 #   print(number_acc))


    return "number_acc"


print(mask_account_card("Счет 73654108430135874305"))
print(mask_account_card("Visa Platinum 7000792289606361"))
