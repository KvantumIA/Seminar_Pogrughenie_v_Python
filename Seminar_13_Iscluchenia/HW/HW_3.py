"""
В организации есть два типа людей: сотрудники и обычные люди. Каждый человек
(и сотрудник, и обычный) имеет следующие атрибуты:

Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка,
не пустая) Возраст (целое положительное число) Сотрудники имеют также
уникальный идентификационный номер (ID), который должен быть шестизначным
положительным целым числом.

Ваша задача:

Создать класс Person, который будет иметь атрибуты и методы для управления
данными о людях (Фамилия, Имя, Отчество, Возраст). Класс должен проверять
валидность входных данных и генерировать исключения InvalidNameError и
InvalidAgeError, если данные неверные.

Создать класс Employee, который будет наследовать класс Person и добавлять
уникальный идентификационный номер (ID). Класс Employee также должен проверять
валидность ID и генерировать исключение InvalidIdError, если ID неверный.

Добавить метод birthday в класс Person, который будет увеличивать возраст
человека на 1 год.

Добавить метод get_level в класс Employee, который будет возвращать уровень
сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).

Создать несколько объектов класса Person и Employee с разными данными и
проверить, что исключения работают корректно при передаче неверных данных.
"""


class InvalidNameError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(
            f'Invalid name: {value}. Name should be a non-empty string.')


class InvalidAgeError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(
            f'Invalid age: {value}. Age should be a positive integer.')


class InvalidIdError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(
            f'Invalid id: {value}. Id should be a 6-digit positive integer between 100000 and 999999.')


class Person:
    def __init__(self, last_name: str, first_name: str, surname: str,
                 age: int):
        self.last_name = last_name
        self.first_name = first_name
        self.surname = surname
        self.age = age

    def birthday(self):
        return self.age + 1

    def get_age(self):
        return self.age

    def __setattr__(self, key, value):
        if key == 'age':
            if isinstance(value, int) and value < 0:
                raise InvalidAgeError(value)
            else:
                super.__setattr__(self, key, value)
        else:
            if isinstance(value, str) and value == '':
                raise InvalidNameError(value)
            else:
                super.__setattr__(self, key, value)

    def __str__(self):
        return (f'Фамилия: {self.last_name}\n'
                f'Имя: {self.first_name}\n'
                f'Отчество: {self.surname}\n'
                f'Возраст: {self.age}\n')


class Employee(Person):
    def __init__(self, last_name, first_name, surname, age, id_num: int):
        super().__init__(last_name, first_name, surname, age)
        self.id = id_num

    def get_level(self):
        return int((sum(int(i) for i in str(self.id)))/7)

    def __setattr__(self, key, value):
        if key == 'id':
            if isinstance(value, int) and (len(str(value)) < 6 or value < 0):
                raise InvalidIdError(value)
        super.__setattr__(self, key, value)

    def __str__(self):
        return (f'Фамилия: {self.last_name}\n'
                f'Имя: {self.first_name}\n'
                f'Отчество: {self.surname}\n'
                f'Возраст: {self.age}\n'
                f'ID: {self.id}')


# person = Person("a", "f", "Doe", 1)
# print(person)

# p1 = Person('kor', 'ivan', 'alex', 34)
# p2 = Person('Alev', 'Vol', 'Iv', 23)
# print(p1)
# print(p2)
# e1 = Employee('Era', 'war', 'vel', 23, 123456)
# print(e1.get_level())
# print(e1)

employee = Employee("Bob", "Johnson", "Brown", 40, 12345)
