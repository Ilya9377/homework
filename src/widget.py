from datetime import datetime

from src.masks import account_number, number_card


def hides_data(input_str: str) -> str:
    """
    Функция возвращает тип карты/счета и скрытый номер карты/счета
    :param input_str: str
    :return: str
    """
    input_lst = input_str.split(" ")
    if input_lst[0] == "Счет":
        return str(input_lst[0] + " " + account_number(input_lst[1]))
    else:
        return str(" ".join(input_lst[:-1]) + " " + number_card(input_lst[-1]))


def convert_data(data: str) -> str:
    """Преобразование строки в объект даты и времени
    Формат строки включает миллисекунды, поэтому нужно использовать формат "%f" для них"""
    date_format = "%Y-%m-%dT%H:%M:%S.%f"
    return datetime.strptime(data, date_format).strftime("%d.%m.%Y")
