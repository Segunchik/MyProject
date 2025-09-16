import os
from src.decorators import log


def test_log_success(capsys) -> None:
    @log()
    def add_num(x: int, y: int) -> int:
        return x + y

    add_num(2, 3)
    captured = capsys.readouterr()
    assert "Статус: успешно\n" in captured.out
    assert "Результат: 5\n" in captured.out


def test_log_typeerror(capsys) -> None:
    @log()
    def add_num(x: int, y: int) -> int:
        return x + y

    add_num("2", 3)
    captured = capsys.readouterr()
    assert "Тип ошибки: TypeError\n" in captured.out


def test_log_creating_file():
    file_path = "test_log.txt"

    @log(file_path)
    def add_num(a, b):
        return a + b

    add_num(3, 5)

    assert os.path.exists(file_path)
    os.remove(file_path)


def test_log_data_in_file():
    file_path = "test_log.txt"

    @log(file_path)
    def add_num(a, b):
        return a + b

    add_num(3, 5)

    with open(file_path, "r", encoding="utf-8") as file:
        data_file = file.read()
        assert "Функция: add_num" in data_file
        assert "Результат: 8" in data_file
    os.remove(file_path)
