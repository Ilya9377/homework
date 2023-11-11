from typing import Any


def filter_by_currency(list_dict: list[dict], valyta) -> Any:
    return (i for i in list_dict if i["operationAmount"]["currency"]["code"] == valyta)


def transaction_descriptions(transactions: list[dict]) -> Any:
    return (i["description"] for i in transactions )


def convert_to_card_number(num) -> str:
    """Функция для конвертации номера крты по заданому числу"""
    mask = "0000 0000 0000 0000"
    s = ""
    for i, c in enumerate(str(num)[::-1]):
        if i % 4 == 0:
            s += " "
        s += c
    return mask[:len(mask) - (len(s) - 1)] + s[::-1]


def card_number_generator(start: int, end: int):
    """генератор номемеров заданых карт в заданом диапазоне"""
    return (convert_to_card_number(i) for i in range(start, end + 1))
