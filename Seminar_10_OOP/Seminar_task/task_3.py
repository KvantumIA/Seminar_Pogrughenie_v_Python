# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.__age = age

    def full_name(self):
        return f'My name is {self.name + " " + self.surname} and my age is {self.__age}'

    def birthday(self):
        self.__age += 1

    def age(self):
        return self.__age


if __name__ == '__main__':
    p1 = Person('Jack', 'Daniels', 25)
    print(p1.full_name())

