# MyProject

## Описание:

Проект MyProject - это разработка виджета банковских операций клиента

## Установка:

Клонируйте репозиторий:
```
git clone https://github.com/Segunchik/MyProject.git
```

## Требования:
- Python 3.8+
- Poetry (менеджер зависимостей)
- Pytest (фреймворк для тестирования)
- pytest-cov (библиотека для анализа покрытия тестами)
## Установка Poetry
### Для Linux/macOS
```
curl -sSL https://install.python-poetry.org | python3 -
```
#### Для Windows (PowerShell)
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```
### После установки добавьте Poetry в PATH:
```
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc  # или .zshrc
source ~/.bashrc
```
## Установка Pytest
'''
poetry add --group dev pytest
'''

## Установка pytest-cov
'''
poetry add --group dev pytest-cov
'''

## Установка библиотеки pandas
'''
poetry add pandas
'''

## Установка приложения:

Клонируйте репозиторий:
```
git clone https://github.com/Segunchik/MyProject.git
```

## Конфигурация
### Файл ``pyproject.toml`` содержит все настройки проекта и зависимости.

## Модули:
### Модуль masks.py содержит функции:
#### - get_mask_card_number(card_number: int) - маскирует номер каты
#### - get_mask_account(account_number: int) - маскирует номер счета

### Модуль widget.py содержит функции:
#### - mask_account_card(account_card: str) - маскирует номер карты или счета, в зависимости от типа
#### - get_date(date_string: str) - Преобразует строку с датой из формата "2024-03-11T02:26:18.671407" в формат ДД.ММ.ГГГГ.

### Модуль processing.py содержит функции:
#### - filter_by_state(data: list, state: str = "EXECUTED") -> list: - Фильтрует список словарей по значению ключа state.
#### - sort_by_date(data_list: list, reverse = True) -> list: - Сортирует список словарей по дате в поле 'date'.

### Модуль generators.py содержит функции:
#### - filter_by_currency(transactions: list, currency: str = "USD") -> Iterator[dict]: - Фильтрует список транзакций по ключу currency
#### - transaction_descriptions(transactions: list) -> list: - принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
#### - card_number_generator(start: int, end: int) -> Generator[str, Any, None]: - Функция генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.

### Модуль decorators.py содержит функцию:
#### - log - Декоратор для логирования вызовов функций с возможностью записи в файл. Регистрирует время вызова, имя функции, аргументы, результат и ошибки.


### Модуль data_file_reader.py содержит функции:
#### - csv_reader(path_file: str) -> list[dict]|str: - Читает файл формата csv и возвращает список словарей с его содержимым.
#### - excel_reader(path_file: str) -> list[dict]|str: - Функция принимает на вход путь к файлу в формате EXCEL и возвращает список словарей с его содержимым