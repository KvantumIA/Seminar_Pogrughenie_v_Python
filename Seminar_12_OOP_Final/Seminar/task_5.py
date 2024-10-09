"""Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера."""

class Valid:

    def __init__(self, min_value: float = None, max_value: float = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not self.min_value < value < self.max_value:
            raise ValueError(f'{value} is lesser than {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'{value} is greater than {self.max_value}')


class Rectangle:
    width = Valid(1, 100)
    length = Valid(1, 200)

    def __init__(self, width: float, length: float = None) -> None:
        self.width = width
        self.length = width if length is None else length

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.length)

    def get_area(self) -> float:
        return self.width * self.length

    def __str__(self):
        return (f'\nRectangle: {self.width} X {self.length}'
                f'\nPerimeter: {self.get_perimeter()}'
                f'\nArea:      {self.get_area()}')
    #
    # def __repr__(self):
    #     return f'Rectangle({self.width}, {self.length})'


a = Rectangle(10, 10)
print(a)