import logging


logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает номер карты в виде числа и возвращает маску карты в виде XXXX XX** **** XXXX

    Параметр:
    card_number(int): целое число с номером карты

    Возвращает строку с замаскированным номером карты
    """

    logger.info(f"Проверяем, является ли {card_number} номером карты")
    if isinstance(card_number, int) and len(str(card_number)) == 16:
        logger.info("Успешно")
        # Преобразуем номер в строку
        card_number_str = str(card_number)
        mask_cardnumber = "".join(
            card_number_str[:4] + " " + card_number_str[4:6] + "** ****" + " " + card_number_str[12:]
        )
        logger.info(f"Замаскированный номер карты {mask_cardnumber}")
        return mask_cardnumber

    else:
        logger.info("Некорректный номер карты")
        return "Введен некорректный номер карты"


def get_mask_account(account_number: int) -> str:
    """
    Функция принимает номер счета и возвращает маску в виде ** ХХХХ

    Параметр:
    account_number(int): целое число с номером счета

    Возвращает строку с замаскированным номером счета
    """
    logger.info(f"Проверяем, является ли {account_number} номером счета")
    if isinstance(account_number, int) and len(str(account_number)) == 20:
        logger.info("Успешно")
        account_number_str = str(account_number)
        mask_account_number = "".join("**" + account_number_str[-4:])
        logger.info(f"Замаскированый номер счета {mask_account_number}")
        return mask_account_number
    else:
        logger.info("Некорректный номер счета")
        return "Введен некорректный номер счета"
