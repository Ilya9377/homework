from src.masks import number_card, account_number


def hides_data(input_str: str) -> str:
    """
    Функция возвращает тип карты/счета и скрытый номер карты/счета
    :param input_str: str
    :return: str
    """
    input_lst = input_str.split(" ")
    if input_lst[0] == "Счет":
        return input_lst[0] + " " + account_number(input_lst[1])
    else:
        return input_lst[0] + " " + number_card(input_lst[1])
