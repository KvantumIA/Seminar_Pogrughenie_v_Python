# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

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
    group_ext = {'txt': 3, 'jpg': 2, 'md': 4}
    create_group_f(group_ext)

