# Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту директорию и все вложенные директории.
# Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle. Каждый результат должен содержать следующую информацию:

# Путь к файлу или директории: Абсолютный путь к файлу или директории. Тип объекта: Это файл или директория. Размер: Для файлов - размер в
# байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах. Важные детали:

# Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.

# Для файлов сохраните их размер в байтах.

# Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной директории, и вложенных директорий.

# Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
# Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.
# Для обхода файловой системы вы можете использовать модуль os.

# Вам необходимо написать функцию traverse_directory(directory), которая будет выполнять обход директории и возвращать результаты в виде списка словарей.
# После этого результаты должны быть сохранены в трех различных файлах (JSON, CSV и Pickle) с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.
# Файлы добавляются в список results в том порядке, в котором они встречаются при рекурсивном обходе директорий. При этом сначала добавляются файлы, а затем директории.

# Для каждого файла (name в files), сначала создается полный путь к файлу (path = os.path.join(root, name)), и затем получается размер файла (size = os.path.getsize(path)).
# Информация о файле добавляется в список results в виде словаря {'Path': path, 'Type': 'File', 'Size': size}.
# Затем, для каждой директории (name в dirs), также создается полный путь к директории (path = os.path.join(root, name)), и вызывается функция get_dir_size(path),
# чтобы получить размер всей директории с учетом ее содержимого. Информация о директории добавляется в список results в виде словаря
# {'Path': path, 'Type': 'Directory', 'Size': size}.

import os
import json
import pickle
import csv


def save_results_to_json(json_data, name):
    with open(name, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)


def save_results_to_csv(json_data, name):
    with open(name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Path', 'Type', 'Size'])
        writer.writeheader()
        for item in json_data:
            writer.writerow(item)


def save_results_to_pickle(pickle_data, name):
    with open(name, 'wb') as f:
        pickle.dump(pickle_data, f)


def get_dir_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def traverse_directory(path):
    """Выполняет обход директории и возвращает результаты в виде списка словарей"""
    results = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            size = os.path.getsize(file_path)
            results.append({
                'Path': file_path,
                'Type': 'File',
                'Size': size,
            })
        for dirname in dirnames:
            dir_path = os.path.join(dirpath, dirname)
            size = get_dir_size(dir_path)
            results.append({
                'Path': dir_path,
                'Type': 'Directory',
                'Size': size,
            })

    return results


# {'Path': path, 'Type': 'File', 'Size': size}
path = 'test'
print(traverse_directory(path))

save_results_to_json(traverse_directory(path), 'results.json')
save_results_to_csv(traverse_directory(path), 'results.csv')
save_results_to_pickle(traverse_directory(path), 'results.pickle')


# [
# {'Path': 'geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457},
# {'Path': 'geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21},
# {'Path': 'geekbrains/covid.json', 'Type': 'File', 'Size': 35228079},
# {'Path': 'geekbrains/input2.txt', 'Type': 'File', 'Size': 9},
# {'Path': 'geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21},
# {'Path': 'geekbrains/age_report.csv', 'Type': 'File', 'Size': 85},
# {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 171},
# {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 171},
# {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171},
# {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101},
# {'Path': 'geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70}
# ]
#

# Ваш ответ:
#
# {'california_housing_train.csv': {'Path': '/cps/ZNIZ8ROTOL/geekbrains/california_housing_train.csv', 'Type': 'File', 'Size': 1457},
# 'student_performance.txt': {'Path': '/cps/ZNIZ8ROTOL/geekbrains/student_performance.txt', 'Type': 'File', 'Size': 21},
# 'covid.json': {'Path': '/cps/ZNIZ8ROTOL/geekbrains/covid.json', 'Type': 'File', 'Size': 35228079},
# 'input2.txt': {'Path': '/cps/ZNIZ8ROTOL/geekbrains/input2.txt', 'Type': 'File', 'Size': 9},
# 'avg_list.txt': {'Path': '/cps/ZNIZ8ROTOL/geekbrains/avg_list.txt', 'Type': 'File', 'Size': 21},
# 'age_report.csv': {'Path': '/cps/ZNIZ8ROTOL/geekbrains/age_report.csv', 'Type': 'File', 'Size': 85},
# 'fruits.csv': {'Path': '/cps/ZNIZ8ROTOL/geekbrains/my_ds_projects/My-code/GB_data/fruits.csv', 'Type': 'File', 'Size': 101},
# 'list_of_names.txt': {'Path': '/cps/ZNIZ8ROTOL/geekbrains/my_ds_projects/My-code/GB_data/list_of_names.txt', 'Type': 'File', 'Size': 70},
# 'my_ds_projects': {'Path': '/cps/ZNIZ8ROTOL/geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 171},
# 'My-code': {'Path': '/cps/ZNIZ8ROTOL/geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 171},
# 'GB_data': {'Path': '/cps/ZNIZ8ROTOL/geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'Directory', 'Size': 171}}

# [{'Path': 'geekbrains', 'Type': 'File', 'Size': 1457},
# {'Path': 'geekbrains', 'Type': 'File', 'Size': 21},
# {'Path': 'geekbrains', 'Type': 'File', 'Size': 35228079},
# {'Path': 'geekbrains', 'Type': 'File', 'Size': 9},
# {'Path': 'geekbrains', 'Type': 'File', 'Size': 21},
# {'Path': 'geekbrains', 'Type': 'File', 'Size': 85},
# {'Path': 'geekbrains', 'Type': 'Directory', 'Size': 171},
# {'Path': 'geekbrains/my_ds_projects', 'Type': 'Directory', 'Size': 171},
# {'Path': 'geekbrains/my_ds_projects/My-code', 'Type': 'Directory', 'Size': 171},
# {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'File', 'Size': 101},
# {'Path': 'geekbrains/my_ds_projects/My-code/GB_data', 'Type': 'File', 'Size': 70}]
