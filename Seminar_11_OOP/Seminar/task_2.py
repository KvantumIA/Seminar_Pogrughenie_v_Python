'''Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков архивов
list-архивы также являются свойствами экземпляра'''


class MyClass:
    """Задача для семинара: мой класс добавляет свойства к классу."""

    _my_list = []

    def __init__(self, number, mystr):
        self.number = number
        self.my_str = mystr

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.archive = MyClass._my_list.copy()
        MyClass._my_list.append(instance)
        return instance

    def __repr__(self):
        return f'MyClass("{self.number}", "{self.my_str}")'

    def __str__(self):
        return f'Добавлены свойства экземпляра {self.number} и {self.my_str}'


cl_1 = MyClass('1', 'Hello')
cl_2 = MyClass('2', 'Привет')
cl_3 = MyClass('3', 'Hi')

# a = eval(cl_1.__repr__())
# print(a)
# print(repr(a))
print([cl_1])
# print(cl_1)

