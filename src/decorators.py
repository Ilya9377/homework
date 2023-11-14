from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[..., Any]:
    """Декоратор для логирования ошибок выполнения функции."""

    def my_decor(function: Callable[..., int]) -> Any:
        """Внутренний декоратор для реализации логирования."""

        @wraps(function)
        def inner(*args: tuple[int], **kwargs: dict[int, int]) -> Any:
            """Внутренняя функция, выполняющая логирование и вызов целевой функции."""
            data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = function(*args, **kwargs)
                if filename:
                    with open(filename, "a") as f:
                        f.write(f"{data} {function.__name__} ok\n")
                else:
                    print(f"{data} {function.__name__} ok\n")
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a") as f:
                        f.write(f"{data} {function.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                        return 0
                else:
                    print(f"{data} {function.__name__} error: {e}. Inputs: {args}, {kwargs}\n")

        return inner

    return my_decor


# @log(filename="mylog.txt")
# def my_function(x: Any, y: Any) -> Any:
#     return x + y
