from typing import Any

import pytest

from src.add_task import count_number_in_list


@pytest.fixture
def my_num_list() -> tuple[list[Any], int]:
    return [1, 2, 5, 5, 6, 5, 3, 6], 5


def test_count_number_in_list(my_num_list: tuple[list[Any], int]) -> Any:
    assert count_number_in_list(my_num_list[0], my_num_list[1]) == 3
