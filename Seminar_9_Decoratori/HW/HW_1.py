"""Генерация случайных данных и нахождение корней квадратного уравнения

Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайны числа в каждой строке, от 100-1000 строк, и записывать их в CSV-файл.
Функция принимает два аргумента:

    file_name (строка) - имя файла, в который будут записаны данные.
    rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.

Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида ax^2 + bx + c = 0. Функция принимает три аргумента:

    a, b, c (целые числа) - коэффициенты квадратного уравнения.

Функция возвращает:
    None, если уравнение не имеет корней (дискриминант отрицателен).
    Одно число, если уравнение имеет один корень (дискриминант равен нулю).
    Два числа (корни), если уравнение имеет два корня (дискриминант положителен).

Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. Декоратор выполняет следующие действия:
Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json будет сохранена информация о параметрах и результатах вычислений
для каждой строки данных из CSV-файла.

Пример

На входе:
    generate_csv_file("input_data.csv", 101)
    find_roots("input_data.csv")

    with open("results.json", 'r') as f:
        data = json.load(f)

    if 100<=len(data)<=1000:
        print(True)
    else:
        print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

    print(len(data)==101)


На выходе:
True
True

Формат JSON файла определён следующим образом:
[
    {"parameters": [a, b, c], "result": result},
    {"parameters": [a, b, c], "result": result},
    ...
]"""

import cmath
import json
import random
import csv
from typing import Callable


def generate_csv_file(file_name, rows):
    csv_data = []
    for _ in range(rows):
        csv_data.append([random.randint(100, 1000) for _ in range(3)])
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for item in csv_data:
            writer.writerow(item)


def save_to_json(func: Callable):
    def wrapper(*args, **kwargs):
        csv_file = args[0]
        csv_data = []
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                csv_data.append({'parameters': [a, b, c], 'result': result})

        with open('results.json', 'w', encoding='utf-8') as f:
            json.dump(csv_data, f, indent=4, ensure_ascii=False)

    return wrapper


@save_to_json
def find_roots(a, b, c):
    """ax^2 + bx + c = 0"""
    D = b**2 - 4*a*c
    if D < 0:
        return None
    elif D == 0:
        """Одно число, если уравнение имеет один корень (дискриминант равен нулю)."""
        x = -b / (2 * a)
        return x,
    else:
        """Два числа (корни), если уравнение имеет два корня (дискриминант положителен)."""
        x1 = (-b + cmath.sqrt(D).real) / (2 * a)
        x2 = (-b - cmath.sqrt(D).real) / (2 * a)
        return x1, x2


generate_csv_file('input_data.csv', 101)
find_roots("input_data.csv")

with open("results.json", 'r') as f:
    data = json.load(f)

if 100 <= len(data) <= 1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")

print(len(data) == 101)
