"""Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр
прямоугольника.
Складываем и вычитаем периметры, а не длину и ширину.
При вычитании не допускайте отрицательных значений."""

from functools import total_ordering


@total_ordering
class Rectangle:
    def __init__(self, hight, _len):
        self.hight = hight
        self.len = _len

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.hight + other.hight, self.len + other.len)

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            new_hight = self.hight - other.hight
            new_len = self.len - other.len
            if new_hight > 0 and new_len > 0:
                return Rectangle(new_hight, new_len)
            else:
                return f'Невозможное значение'

    def __str__(self):
        return f'Прямоугольник со сторонами {self.hight} и {self.len}'

    def area(self):
        return self.hight * self.len

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        return f'Невозможно сравнить эти объекты'

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        return f'Невозможно сравнить эти объекты'


a = Rectangle(10, 20)
b = Rectangle(10, 20)

print(a == 5)
print(a <= b)
