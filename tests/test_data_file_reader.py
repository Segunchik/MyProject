import pandas as pd
import pytest
from unittest.mock import patch
from src.data_file_reader import csv_reader, excel_reader


@patch("pandas.read_csv")
def test_csv_reader(mock_read_csv):
    mock_read_csv.return_value.to_dict.return_value = [{"amount": 100},{"amount1": 1000}]
    result = csv_reader("test.csv")
    assert result == [{"amount": 100},{"amount1": 1000}]
    mock_read_csv.assert_called_once_with("test.csv",delimiter=';')


def test_csv_reader_file_not_found():
    with patch("builtins.open") as mock_file:
        mock_file.side_effect = FileNotFoundError("Файл не найден")
        result = csv_reader("non_existent.csv")
    assert result == "Файл не найден"


def test_excel_reader_success():
    excel_data = pd.DataFrame({
        "name": ["Анна", "Борис"],
        "age": [25, 30],
        "city": ["Москва", "Санкт-Петербург"]
    })

    with patch("pandas.read_excel") as mock_read_excel:
        mock_read_excel.return_value = excel_data
        result = excel_reader("test.xlsx")

    expected = [
        {"name": "Анна", "age": 25, "city": "Москва"},
        {"name": "Борис", "age": 30, "city": "Санкт-Петербург"}
    ]

    assert result == expected


def test_excel_reader_file_not_found():
    with patch("pandas.read_excel") as mock_read_excel:
        mock_read_excel.side_effect = FileNotFoundError("Файл не найден")
        result = excel_reader("non_existent.xlsx")
    assert result == "Файл не найден"
