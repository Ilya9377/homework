from typing import Any


def check_letter(input_list: list[Any]) -> list[Any]:
    """Функция проверяет длину скиска и
    возвращает список строк, в которых первая и последняя буквы совпадают"""
    return list(filter(lambda x: len(x) > 0 and x[0] == x[-1], input_list))


def max_two_number(input_list: list[Any]) -> Any:
    """ Функция проверяет длину скиска и
    возвращает максимальное произведение двух чисел из списка"""
    if len(input_list) < 2:
        return 0
    sort_list = sorted(input_list)
    return max(sort_list[0] * sort_list[1], sort_list[-1] * sort_list[-2])


def spisok_sort(data: list[Any], category: str = "") -> list[Any]:
    """
    Фунция возвращает отсортированый по стоймости продуктов список словарей.
    Если задана категория, то сортировка происходит только в этой категории, если нет
    то весь список целиком
    :param data: list
    :param category: str
    :return: list
    """
    if category != "":
        result = []
        for diction in data:
            if diction["category"] == category:
                result.append(diction)
        return sorted(result, key=lambda x: x["price"], reverse=True)
    else:
        return sorted(data, key=lambda x: x["price"], reverse=True)


def count_number_in_list(num_list: list[Any], num: int) -> int:
    return num_list.count(num)
