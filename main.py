import os.path

from src.data_file_reader import csv_reader, excel_reader
from src.processing import filter_by_state, sort_by_date, process_bank_search
from src.utils import read_json_file
from src.widget import get_date


def main() -> None:
    """
    Функция main в модуле main, которая отвечает за основную логику проекта и связывает функциональности между собой.
    :return:
    """

    current_dir = os.path.dirname(__file__)
    json_file_path = os.path.join(current_dir, "data", "operations.json")
    csv_file_path = os.path.join(current_dir, "data", "transactions.csv")
    excel_file_path = os.path.join(current_dir, "data", "transactions_excel.xlsx")
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        print(
            """
            Выберите необходимый пункт меню:
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла
            """
        )
        choice_file_type = int(input("Пользователь: ").strip())
        if choice_file_type in {1, 2, 3}:
            break
        print("Некорректный ввод. Попробуйте еще раз.")

    if choice_file_type == 1:
        print("Для обработки выбран json-файл")
        data_file = read_json_file(json_file_path)
    if choice_file_type == 2:
        print("Для обработки выбран csv-файл")
        data_file = csv_reader(csv_file_path)
    if choice_file_type == 3:
        print("Для обработки выбран excel-файл")
        data_file = excel_reader(excel_file_path)

    while True:
        print(
            """
            Введите статус, по которому необходимо выполнить фильтрацию.
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
            """
        )
        choice_status = input("Пользователь: ").strip().upper()
        if choice_status in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Операции отфильтрованы по статусу "{choice_status}"')
            filtered_by_status = filter_by_state(data_file, choice_status)
            break
        else:
            print(f'Статус операции "{choice_status}" недоступен.')

    choice_sort_date = (
        input(
            """
        Отсортировать операции по дате? Да/Нет
        """
        )
        .lower()
        .strip()
    )
    if choice_sort_date == "да":
        choice_direction_sort_date = (
            input(
                """
            Отсортировать по возрастанию или по убыванию?
            """
            )
            .lower()
            .strip()
        )
        if choice_direction_sort_date == "по возрастанию":
            sorted_by_date = sort_by_date(filtered_by_status, reverse=False)
        elif choice_direction_sort_date == "по убыванию":
            sorted_by_date = sort_by_date(filtered_by_status)
    else:
        sorted_by_date = filtered_by_status

    choice_currency = (
        input(
            """
        Выводить только рублевые транзакции? Да/Нет
        """
        )
        .lower()
        .strip()
    )
    if choice_currency == "да":
        filtered_data = [
            x
            for x in sorted_by_date
            if x.get("currency_code") == "RUB"
            or x.get("currency") == "RUB"
            or x.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
        ]
    else:
        filtered_data = sorted_by_date

    search_answer = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет ").strip().lower()
    if search_answer == "да":
        word = input("Введите слово для фильтрации: ").strip()
        filtered_data = process_bank_search(filtered_data, word)

    print("Программа: Распечатываю итоговый список транзакций...")
    if not filtered_data:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(filtered_data)}\n")
        if choice_file_type == 1:
            for item in filtered_data:
                print(f"{get_date(item.get('date'))} {item.get('description')}")
                print(f"{item.get('from')} -> {item.get('to')}")
                print(
                    f"Сумма: "
                    f"{item.get('operationAmount', {}).get('amount')} "
                    f'{item.get("operationAmount", {}).get("currency", {}).get("name")}\n'
                )
        elif choice_file_type == 2 or choice_file_type == 3:
            for item in filtered_data:
                print(f"{get_date(item.get('date'))} {item.get('description')}")
                print(f"{item.get('from')} -> {item.get('to')}")
                print(f"Сумма: {item.get('amount')} {item.get('currency_name')}\n")


main()
