# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
from pathlib import Path

from task_2_Random_name import random_name
from random import randbytes, randint
import os


def create_file(extension, min_len=6, max_len=30, min_size=256, max_size=4096, file_count=42):
    for _ in range(file_count):
        with open(f'test_dir/{random_name(min_len, max_len)}.{extension}', 'wb') as f:
            f.write(randbytes(randint(min_size, max_size)))


def create_group_f(group_ext):
    for key, value in group_ext.items():
        create_file(key, file_count=value)


def path_exist(path):
    if not os.path.exists(path):
        Path(path).mkdir()


if __name__ == '__main__':
    create_file('txt', file_count=10)

