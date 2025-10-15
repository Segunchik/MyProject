import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def read_json_file(path: str) -> list[dict[str, Any]]:
    """
    Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых
    транзакциях. Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        file_path = Path(path)
        if not file_path.exists():
            logger.error("Файл не существует")
            raise FileNotFoundError

        with open(file_path, "r", encoding="utf-8") as file:
            logger.info(f"Открываем файл {path}")
            data = json.load(file)
            logger.info("Проверяем содержит ли файл список")
            if isinstance(data, list):
                logger.info("Возвращаем список словарей из файла")
                return data
            else:
                logger.error("Неверный формат данных в файле")
                raise ValueError

    except json.JSONDecodeError as er:
        logger.error(f"Ошибка {er}")
        return []
    except FileNotFoundError as er:
        logger.error(f"Ошибка {er}")
        return []
    except ValueError as er:
        logger.error(f"Ошибка {er}")
        return []
