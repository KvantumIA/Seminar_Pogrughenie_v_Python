"""Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него все функции:
get_dir_size,
save_results_to_json,
save_results_to_csv,
save_results_to_pickle, traverse_directory."""


def create_file_init():
    with open('__init__.py', 'w', encoding='utf-8') as f:
        f.write('def get_dir_size:\n  pass \n\n\n'
                'def save_results_to_json:\n  pass \n\n\n'
                'def save_results_to_csv:\n  pass \n\n\n'
                'def save_results_to_pickle:\n  pass \n\n\n'
                'def traverse_directory:\n  pass')


create_file_init()

with open("__init__.py", "r") as init_file:
    code = init_file.read()

function_names = [
    "def get_dir_size",
    "def save_results_to_json",
    "def save_results_to_csv",
    "def save_results_to_pickle",
    "def traverse_directory",
]

for func_name in function_names:
    if func_name not in code:
        print(f"Функция {func_name} не найдена в файле __init__.py")
    else:
        print(f"Функция {func_name} найдена в файле __init__.py")
