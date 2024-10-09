"""Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1."""


class GenFactorial:
    def __init__(self, *args):
        self.start, self.step = 1, 1
        match args:
            case [stop]:
                self.stop = stop
            case [start, stop]:
                self.start, self.stop = start, stop
            case [start, stop, step]:
                self.start, self.stop, self.step = start, stop, step
            case _:
                raise ValueError()

    @staticmethod
    def factorial(n):
        if n in (0, 1):
            return 1
        elif n < 0:
            raise ValueError("Can't be less then 0")
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.stop:
            temp = self.factorial(self.start)
            self.start += self.step
            return temp
        raise StopIteration


a = GenFactorial(2, 14, 3)
print(*a)


