import json
import os
from pathlib import Path

from src.utils import read_json_file


def test_valid_file():
    # Создаем тестовый JSON файл
    test_data = [{"id": 1, "amount": 100.0, "currency": "RUB"}, {"id": 2, "amount": 200.0, "currency": "USD"}]
    test_path = Path("test_file.json")

    # Записываем тестовые данные в файл
    with open(test_path, "w", encoding="utf-8") as f:
        json.dump(test_data, f)

    # Проверяем результат
    result = read_json_file(test_path)
    assert result == test_data

    # Удаляем тестовый файл
    os.remove(test_path)


def test_nonexistent_file():
    # Проверяем обработку несуществующего файла
    result = read_json_file("nonexistent_file.json")
    assert result == []


def test_empty_file():
    # Создаем пустой JSON файл
    test_path = Path("empty_file.json")
    test_path.touch()

    # Проверяем результат
    result = read_json_file(test_path)
    assert result == []

    # Удаляем тестовый файл
    os.remove(test_path)


def test_invalid_json():
    # Создаем файл с некорректным JSON
    test_path = Path("invalid_file.json")
    with open(test_path, "w", encoding="utf-8") as f:
        f.write("{invalid json}")

    # Проверяем результат
    result = read_json_file(test_path)
    assert result == []

    # Удаляем тестовый файл
    os.remove(test_path)


def test_non_list_content():
    # Создаем файл с не-list содержимым
    test_path = Path("non_list_file.json")
    with open(test_path, "w", encoding="utf-8") as f:
        json.dump({"key": "value"}, f)

    # Проверяем результат
    result = read_json_file(test_path)
    assert result == []

    # Удаляем тестовый файл
    os.remove(test_path)
