import json
from pathlib import Path
from typing import Any


def read_json_file(path: str) -> list[dict[str, Any]]:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
    транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        file_path = Path(path)
        if not file_path.exists():
            raise FileNotFoundError

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                raise ValueError

    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
    except ValueError:
        return []
