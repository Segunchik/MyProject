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
    return sorted(data_list, key=lambda x: x["date"], reverse=reverse)
