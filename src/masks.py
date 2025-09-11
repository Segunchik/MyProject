def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает номер карты в виде числа и возвращает маску карты в виде XXXX XX** **** XXXX

    Параметр:
    card_number(int): целое число с номером карты

    Возвращает строку с замаскированным номером карты
    """
    if isinstance(card_number, int) and len(str(card_number)) == 16:
        # Преобразуем номер в строку
        card_number_str = str(card_number)
        mask_cardnumber = "".join(
            card_number_str[:4]
            + " "
            + card_number_str[4:6]
            + "** ****"
            + " "
            + card_number_str[12:]
        )
        return mask_cardnumber

    else:
        return "Введен некорректный номер карты"


def get_mask_account(account_number: int) -> str:
    """
    Функция принимает номер счета и возвращает маску в виде ** ХХХХ

    Параметр:
    account_number(int): целое число с номером счета

    Возвращает строку с замаскированным номером счета
    """

    if isinstance(account_number, int) and len(str(account_number)) == 20:
        account_number_str = str(account_number)

        return "".join("**" + account_number_str[-4:])
    else:
        return "Введен некорректный номер счета"


# if __name__ != "main.py":
#    print(get_mask_card_number(1234567891234567))
#    print(get_mask_account(12345678945613))
