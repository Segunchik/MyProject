import re


def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Фильтрует список словарей по значению ключа state.

    Параметры:
    data (list): Список словарей для фильтрации
    state (str): Значение ключа state для фильтрации (по умолчанию 'EXECUTED')

    Возвращает:
    list: Новый список словарей, содержащих только те, у которых ключ state соответствует заданному значению
    """

    return [item for item in data if item.get("state") == state]


def sort_by_date(data_list: list, reverse=True) -> list:
    """
    Сортирует список словарей по дате в поле 'date'.

    Параметры:
    data (list): Список словарей для сортировки
    descending (bool): Порядок сортировки (True - убывание, False - возрастание)

    Возвращает:
    list: Новый отсортированный список словарей
    """
    return list(sorted(data_list, key=lambda x: x["date"], reverse=reverse))


def process_bank_search(operations: list[dict], search_str: str) -> list[dict]:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых в описании есть данная строка.
    :param operations:
    :param search:
    :return:
    """
    pattern = re.compile(search_str, re.IGNORECASE)

    result: list = [item for item in operations if pattern.search(item["description"])]

    return result


def process_bank_operations(transactions: list[dict], categories: list) -> dict[str, int]:
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.rn:
    """

    result = {category: 0 for category in categories}

    patterns = {}
    for category in categories:
        try:
            patterns[category] = re.compile(category, re.IGNORECASE)
        except re.error as e:
            raise ValueError(f"Некорректный regex-шаблон для категории '{category}': {e}")

    for operation in transactions:
        if not isinstance(operation, dict) or "description" not in operation:
            continue

        description = str(operation["description"])
        for category, pattern in patterns.items():
            if pattern.search(description):
                result[category] += 1

    return result
