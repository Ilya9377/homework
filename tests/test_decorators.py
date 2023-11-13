from src.decorators import my_function
import pytest, datetime
from typing import Any


@pytest.mark.parametrize(
    "number_1, number_2, expected_result",
    [(1, 2, f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
            f' my_function error: can only concatenate tuple (not "dict") to tuple. Inputs: (1, 2), ' + "{}")]
)
def test_card_number_generator(number_1: int, number_2: int, expected_result: Any) -> Any:
    """тест для функции card_number_generator"""
    my_function(number_1, number_2)
    with open("src/mylog.txt", "r") as f:
        for line in f:
            pass
    assert line.strip() == expected_result


