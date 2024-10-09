"""Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)"""

from datetime import datetime


class MyString(str):
    def __new__(cls, value, name_avtor, *args, **kwargs):
        instance = super().__new__(cls, value)
        return instance

    def __init__(self, value, name_avtor):
        self.name_avtor = name_avtor
        self.time = datetime.now().time()


u_1 = MyString("привет", 'Agata Kristi')
print(u_1.name_avtor)
print(u_1.time)
