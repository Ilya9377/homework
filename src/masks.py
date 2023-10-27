def number_card(user_card: str) -> str:
    """
    Функция для маскировки номера карты
    """
    return user_card[:4] + " " + user_card[4:6] + "** ****" + " " + user_card[-4:]


def account_number(user_account: str) -> str:
    """
    Функция для маскировки номера счета
    """
    return "***" + user_account[-4:]
