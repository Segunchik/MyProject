def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Фильтрует список словарей по значению ключа state.

    """

    return [item for item in data if item.get('state') == state]

