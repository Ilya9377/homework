from src.masks import number_card, account_number
import pytest


@pytest.mark.parametrize("number, expected_result", [("7000792289606361", "7000 79** **** 6361"),
                                                     ("1596837868705199", "1596 83** **** 5199"),
                                                     ("6831982476737658", "6831 98** **** 7658"),
                                                     ("7158300734726758", "7158 30** **** 6758"),
                                                     ("8990922113665229", "8990 92** **** 5229")])
def test_number_card(number, expected_result):
    assert number_card(number) == expected_result


@pytest.mark.parametrize("account, expected_result", [("73654108430135874305", "**4305"),
                                                      ("35383033474447895560", "**5560"),
                                                      ("64686473678894779589", "**9589")])
def test_account_number(account, expected_result):
    assert account_number(account) == expected_result
