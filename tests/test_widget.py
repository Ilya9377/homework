from typing import Any

import pytest

from src.widget import *


@pytest.mark.parametrize(
    "date, expected_result",
    [
        ("2020-08-12T02:26:18.671407", "12.08.2020"),
        ("2019-01-20T02:26:18.671407", "20.01.2019"),
        ("2016-05-01T02:26:18.671407", "01.05.2016"),
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ],
)
def test_convert_data(date: str, expected_result: str) -> Any:
    assert convert_data(date) == expected_result


@pytest.mark.parametrize("input_st, expected_result",
                         [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                          ("Счет 64686473678894779589", "Счет **9589"),
                          ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                          ("Счет 35383033474447895560", "Счет **5560"),
                          ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                          ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
                          ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
                          ("Счет 73654108430135874305", "Счет **4305")])
def test_hides_data(input_st: str, expected_result: str) -> Any:
    assert hides_data(input_st) == expected_result
