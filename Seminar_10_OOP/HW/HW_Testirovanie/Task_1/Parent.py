from Seminar_Pogrugenie_v_Python.Seminar_10_OOP.HW.HW_Testirovanie.Task_1.People import \
    People
from Seminar_Pogrugenie_v_Python.Seminar_10_OOP.HW.HW_Testirovanie.Task_1.Child import \
    Child


class Parent(People):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.list_child = []

    def __repr__(self):
        return f'Parent("{self.name}", "{self.age}")'

    def __str__(self):
        return f'Родитель {self.name}, {self.age}'

    def print_list_child(self):
        return f'Список детей - {self.list_child}'

    @staticmethod
    def feed_change():
        if Child.feed is True:
            Child.feed = False
        else:
            Child.feed = True

    @staticmethod
    def calm_change(new_calm):
        Child.calm = new_calm
