"""
На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.
"""
from functools import total_ordering


@total_ordering
class Rectangle:
    __slots__ = ["_side_a", "_side_b"]

    def __init__(self, side_a, side_b=None):
        self._side_a = side_a
        self._side_b = side_a if side_b is None else side_b

    @property
    def side_a(self):
        return self._side_a

    @side_a.setter
    def side_a(self, value):
        if value > 0:
            self._side_a = value
        else:
            raise ValueError()

    @side_a.getter
    def side_a(self):
        return self._side_a * 10

    def perimeter(self):
        return (self._side_a + self._side_b) * 2

    def area(self):
        return self._side_b * self._side_a

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.perimeter() == other.perimeter()

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.perimeter() < other.perimeter()


if __name__ == '__main__':
    rectangle = Rectangle(5, 4)
    rectangle.perimeter()
