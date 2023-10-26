def number_card(user_card: int) -> str:
    """
    Функция для маскировки номера карты
    """
    s: str = str(user_card)
    return s[:4] + " " + s[4:6] + "** ****" + " " + s[-4:]


def account_number(user_account: int) -> str:
    """
    Функция для маскировки номера счета
    """
    s: str = str(user_account)
    return "***" + s[-4:]
