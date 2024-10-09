""" Создайте три (или более) отдельных классов животных.
 Например рыбы, птицы и т.п.
 У каждого класса должны быть как общие свойства,
 например имя, так и специфичные для класса.
 Для каждого класса создайте метод, выводящий
 информацию специфичную для данного класса.

Доработайте задачу 5.
Вынесите общие свойства и методы классов в класс
Животное.
Остальные классы наследуйте от него.
Убедитесь, что в созданные ранее классы внесены правки."""


class Animals:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    def info(self):
        return f'Меня зовут {self._name}, мне {self.age} лет'

    def set_name(self, name):
        self._name = name


class Birds(Animals):
    def __init__(self, name, age, flight_altitude):
        super().__init__(name, age)
        self.flight_altitude = flight_altitude

    def info(self):
        return super().info() + f' и высота полета {self.flight_altitude}'

    def set_height(self, height):
        self.flight_altitude = height


class Cat(Animals):
    def __init__(self, name, age, run):
        super().__init__(name, age)
        self.run = run

    def set_run(self, len_run):
        self.run = len_run


if __name__ == '__main__':
    duck = Birds('Kryaka', 1, 80)
    print(duck.info())
    cat = Cat('Barsik', 3, 100)
    print(cat.info())
