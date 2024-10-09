# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
import os
from task_4_Create_file import path_exist
from pathlib import Path

FILES_TYPE_DICT = {'Video': ['avi', 'mkv', 'mp4'],
                   'Docs': ['doc', 'txt', 'md'],
                   'Music': ['mp3', 'wav'],
                   'Pictures': ['jpg', 'bmp']}


def sort_files(files_type_dict, path='test_dir', ):
    file_list = os.listdir(path)
    os.chdir(path)
    for file in file_list:
        extension = file.split('.')[1]
        for key, value in files_type_dict.items():
            if extension in value:
                if path_exist(key):
                    os.mkdir(key)
                os.replace(file, os.path.join(key, file))


sort_files(FILES_TYPE_DICT)
