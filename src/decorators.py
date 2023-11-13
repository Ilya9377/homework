import datetime
from typing import Any, Callable


def log(filename: str = "error.txt") -> Callable[..., Any]:
    """Декоратор для логирования ошибок выполнения функции."""
    def my_decor(function: Callable[..., int]) -> Any:
        """Внутренний декоратор для реализации логирования."""
        def inner(*args: tuple[int], **kwargs: dict[int, int]) -> float:
            """Внутренняя функция, выполняющая логирование и вызов целевой функции."""
            with open(filename, "a") as f:
                data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                try:
                    result = function(args, kwargs)
                    f.write(f"{data} {function.__name__} ok\n")
                    return result
                except Exception as e:
                    f.write(f"{data} {function.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                    return 0

        return inner

    return my_decor


@log(filename="src/mylog.txt")
def my_function(x: int, y: int) -> int:
    print(x, y)
    return x + y
