from typing import Any


def check_dict(data: list[Any], state: str = "EXECUTED") -> list[Any]:
    """
    Функия возвращает список словарей с определеным ключем
    :param data: list
    :param state: str
    :return: list
    """
    result = []
    for diction in data:
        if diction["state"] == state:
            result.append(diction)
    return result


def sort_date(data: list[Any], sort: bool = True) -> list[Any]:
    """
    Функия возвращает отсортированый по дате список словарей
    :param data: list
    :param sort: list
    :return: list
    """
    return sorted(data, key=lambda x: x["date"], reverse=sort)
