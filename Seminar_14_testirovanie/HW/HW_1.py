"""
Возьмите задачу Rectangle с прошлых семинаров. Напишите тесты для этой задачи.
Исходный код в редакторе кода надо доработать, чтобы вызывалось исключение
NegativeValueError.

Используйте модуль doctest.

Тесты:

test_width: Тестирование инициализации ширины. Созданы прямоугольники r1 с
шириной 5 и r4 с отрицательной шириной (-2). Убедимся, что r1.width корректно
установлен на 5, а создание r4 вызывает исключение NegativeValueError с текстом
Ширина должна быть положительной, а не {value}

test_height: Тестирование инициализации ширины и высоты. Созданы прямоугольники
r2 с шириной 3 и высотой 4. Проверяем, что r2.width равно 3 и r2.height равно 4
При необходимости выбрасывать исклчение NegativeValueError с текстом Высота
должна быть положительной, а не {value}

test_perimeter: Тестирование вычисления периметра. Создан прямоугольник r1 с
шириной 5 и проверяем, что r1.perimeter() возвращает 20. Также создан
прямоугольник r2 с шириной 3 и высотой 4 и проверяем, что r2.perimeter()
возвращает 14.

test_area: Тестирование вычисления площади. Создан прямоугольник r1 с шириной 5
и проверяем, что r1.area() возвращает 25. Также создан прямоугольник r2 с
шириной 3 и высотой 4 и проверяем, что r2.area() возвращает 12.

test_addition: Тестирование операции сложения. Созданы прямоугольники r1 с
шириной 5 и r2 с шириной 3 и высотой 4. Выполняем операцию сложения r1 + r2 и
проверяем, что полученный прямоугольник r3 имеет правильные значения ширины и
высоты (8 и 6.0 соответственно).

test_subtraction: Тестирование операции вычитания. Созданы прямоугольники r1 с
шириной 5 и r2 с шириной 3 и высотой 4. Выполняем операцию вычитания r1 - r2 и
проверяем, что полученный прямоугольник r3 имеет правильные значения ширины и
высоты (2 и 2.0 соответственно).

Запускать тесты не надо, автотест это сделает сам:

__file__ = None
doctest.testmod(extraglobs={'__file__': __file__})
"""
# Введите ваше решение ниже
import doctest


class NegativeValueError(Exception):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        if self.key == 'width':
            super().__init__(f'Ширина должна быть положительной, а не {value}')
        else:
            super().__init__(f'Высота должна быть положительной, а не {value}')


class Rectangle:
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого

    Тестирование инициализации ширины
    >>> r1 = Rectangle(5)
    >>> r1.width
    5

    >>> try:
    ...     r2 = Rectangle(-2)
    ... except NegativeValueError as e:
    ...     print(e)
    Ширина должна быть положительной, а не -2

    Тестирование инициализации ширины и высоты
    >>> r2 = Rectangle(3, 4)
    >>> r2.width
    3
    >>> r2.height
    4

    Тестирование вычисления периметра
    >>> r1.perimeter()
    20
    >>> r2.perimeter()
    14

    Тестирование вычисления площади
    >>> r1.area()
    25
    >>> r2.area()
    12
    """

    def __init__(self, width, height=None):
        self.width = width
        self.height = height if height is not None else width

    def __setattr__(self, key, value):
        if key in ['width', 'height'] and value <= 0:
            raise NegativeValueError(key, value)
        super().__setattr__(key, value)

    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        return self.width * self.height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников

        Тестирование операции сложения
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 + r2
        >>> r3.width
        8
        >>> r3.height
        6.0
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
            Тестирование операции вычитания
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 - r2
        >>> r3.width
        2
        >>> r3.height
        2.0
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"


if __name__ == '__main__':
    # r1 = Rectangle(5)
    # print(r1.width)
    doctest.testmod()


# Ожидаемый ответ:
#
# **********************************************************************
# , in __main__.Rectangle.__add__
# Failed example:
#     r3.height
# Expected:
#     6.0
# Got:
#     9.0
# **********************************************************************
# , in __main__.Rectangle.__sub__
# Failed example:
#     r3.height
# Expected:
#     2.0
# Got:
#     1.0
# **********************************************************************
# 2 items had failures:
#    1 of   5 in __main__.Rectangle.__add__
#    1 of   5 in __main__.Rectangle.__sub__
# ***Test Failed*** 2 failures.


# Ваш ответ:
#
# **********************************************************************
# , in __main__.Rectangle.__add__
# Failed example:
#     r3.height
# Expected:
#     6.0
# Got:
#     9.0
# **********************************************************************
# , in __main__.Rectangle.__sub__
# Failed example:
#     r4.height
# Expected:
#     2.0
# Got:
#     1.0
# **********************************************************************
# 2 items had failures:
#    1 of   5 in __main__.Rectangle.__add__
#    1 of   5 in __main__.Rectangle.__sub__
# ***Test Failed*** 2 failures.