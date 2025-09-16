from functools import wraps
from time import time
from typing import Any, Callable


def log(filename: str | None = None):  # -> Callable:
    """
    Декоратор для логирования вызовов функций с возможностью записи в файл.
    Регистрирует время вызова, имя функции, аргументы, результат и ошибки.
    """

    def wrapper(function: Callable) -> Callable:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:
            start_time = time()  # Замеряем время начала

            # Формируем строку с аргументами
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)

            try:
                result = function(*args, **kwargs)
                error_info = None
                status = "успешно"

            except Exception as e:
                result = None
                error_info = {"type": type(e).__name__, "message": str(e), "input": signature}
                status = "ошибка"

            end_time = time()  # Замеряем время окончания
            execution_time = end_time - start_time

            # Формируем сообщение для лога
            log_message = (
                f"Функция: {function.__name__}\n"
                f"Статус: {status}\n"
                f"Аргументы: {signature}\n"
                f"Время выполнения: {execution_time:.4f} сек\n"
            )

            if error_info:
                log_message += f"Тип ошибки: {error_info['type']}\n" f"Сообщение: {error_info['message']}\n"
            else:
                log_message += f"Результат: {result}\n"

            # Записываем в файл или выводим в консоль
            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(log_message + "\n")
            else:
                print(log_message)

            return result

        return inner

    return wrapper
