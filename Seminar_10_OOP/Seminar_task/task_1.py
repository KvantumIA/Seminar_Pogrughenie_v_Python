# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
#
PI = 3.14


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def length(self):
        return PI * self.radius * 2

    def area(self):
        return PI * self.radius ** 2


def main():
    circle = Circle(5)

    print(circle.length())
    print(circle.area())


main()