"""Доработаем задачу 1.
Создайте менеджер контекста, который при выходе
сохраняет значения в JSON файл."""

import os
import json


class Factorial:

    def __init__(self, k, file_name='base_fact.json'):
        self._archive_size = k
        self._file_name = file_name
        self.arch = []
        self._last_num = None

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

    def _json_writer(self, new_data):
        data_json = {}
        if os.path.exists(self._file_name):
            with open(self._file_name, 'r', encoding='UTF-8') as file:
                data_json = json.load(file)
        data_json.update(new_data)
        with open(self._file_name, 'w', encoding='UTF-8') as file:
            json.dump(data_json, file)

    def __call__(self, n):
        k_value = Factorial.factorial(n)
        if len(self.arch) >= self._archive_size:
            self.arch.pop(0)
        self.arch.append(k_value)
        self._last_num = n
        return k_value

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._json_writer({str(self._last_num): self.arch[-1]})


with Factorial(3) as a:
    a(4)
    a(3)
    a(2)
    a(5)
    a(6)

print(a.arch)