from src.masks import number_card, account_number


def hides_data(x, y):
    return number_card(x), account_number(y)