"""
На семинаре 13 был создан проект по работе с
пользователями (имя, id, уровень).
Напишите 3-7 тестов pytest для данного проекта.
Используйте фикстуры.
"""

import pytest
from random import randint
from task_5 import Rectangle


@pytest.fixture
def get_rectangle_1():
    # side_a = randint(1, 10)
    # side_b = randint(1, 10)
    return Rectangle(2, 5)


@pytest.fixture
def get_rectangle_2():
    # side_a = randint(1, 10)
    # side_b = randint(1, 10)
    yield Rectangle(2, 5)


def test_equal(get_rectangle_1):
    assert get_rectangle_1.perimeter() == 14


def test_lt(get_rectangle_1):
    assert get_rectangle_1 < Rectangle(3, 5)


def test_lt_(get_rectangle_1):
    assert get_rectangle_1 > Rectangle(1, 5)


if __name__ == '__main__':
    pytest.main(['-v'])
