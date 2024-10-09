"""Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов."""


class Factorial:
    def __init__(self, k):
        self._archive_size = k
        self.arch = []

    @staticmethod
    def factorial(n):
        if n in (0, 1):
            return 1
        elif n < 0:
            raise ValueError("Can't be less then 0")
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    def __call__(self, n):
        k_value = Factorial.factorial(n)
        if len(self.arch) >= self._archive_size:
            self.arch.pop(0)
        self.arch.append(n)
        return k_value


a = Factorial(5)
a(3)
a(4)
a(5)
a(3)
print(a.arch)
