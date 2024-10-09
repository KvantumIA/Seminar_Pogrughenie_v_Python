# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from pathlib import Path
from random import randbytes, randint
import os
from task_2_Random_name import random_name


def create_file(extension, path='test_folder', min_len=6, max_len=30, min_size=256, max_size=4096, file_count=42):
    path_exist(path)
    for i in range(file_count):
        file_name = os.path.join(path, random_name(min_len, max_len)) + '.' + extension
        if os.path.exists(file_name):
            file_name = os.path.join(path, random_name(min_len, max_len) + str(i)) + '.' + extension
        with open(file_name, 'wb') as f:
            f.write(randbytes(randint(min_size, max_size)))


def create_group_f(group_ext):
    for key, value in group_ext.items():
        create_file(key, file_count=value)


def path_exist(path):
    if not os.path.exists(path):
        Path(path).mkdir()


if __name__ == '__main__':
    group_ext = {'txt': 3, 'jpg': 2, 'md': 4, 'avi': 4, 'mpg': 8, 'exe': 3}
    create_group_f(group_ext)
