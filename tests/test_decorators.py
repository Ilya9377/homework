import os.path
from datetime import datetime
from typing import Any

import pytest

from src.decorators import log


@pytest.mark.parametrize(
    "number_1, number_2, expected_result",
    [
        (1, 2, f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} my_function ok'),
        (
            1,
            "0",
            f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
            f" my_function error: unsupported operand type(s)"
            f" for +: 'int' and 'str'. Inputs: (1, '0'), " + "{}",
        ),
    ],
)
def test_my_function(number_1: int, number_2: int, expected_result: str) -> None:
    """тест для функции my_function"""

    if os.path.isdir("tests"):
        patch = "tests/test.txt"
    else:
        patch = "test.txt"
    if os.path.exists(patch):
        os.remove(patch)

    @log(patch)
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(number_1, number_2)
    with open(patch, "r") as f:
        for line in f:
            pass
    assert line.strip() == expected_result


@pytest.mark.parametrize(
    "number_1, number_2, expected_result",
    [
        (
            1,
            2,
            f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} my_function ok'
            # f' my_function error: can only concatenate tuple (not "dict") to tuple. Inputs: (1, 2), ' + "{}",
        ),
        (
            1,
            "0",
            f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
            f" my_function error: unsupported operand type(s)"
            f" for +: 'int' and 'str'. Inputs: (1, '0'), " + "{}",
        ),
    ],
)
def test_console(capsys: Any, number_1: int, number_2: int, expected_result: str) -> None:
    @log()
    def my_function(x: int, y: int) -> int:
        return x + y

    my_function(number_1, number_2)
    log_mess = capsys.readouterr()
    assert log_mess.out.strip() == expected_result
