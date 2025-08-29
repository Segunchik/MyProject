def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Фильтрует список словарей по значению ключа state.

    """

    return [item for item in data if item.get("state") == state]


def sort_by_date(data_list: list, reverse=True) -> list:
    """
    Сортирует список словарей по дате в поле 'date'.
    """
    return sorted(data_list, key=lambda x: x["date"], reverse=reverse)
