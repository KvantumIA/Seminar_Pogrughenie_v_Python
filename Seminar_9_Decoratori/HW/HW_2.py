"""Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.

Создайте файл __init__.py и запишите в него все функции:
save_to_json,
find_roots,
generate_csv_file."""


def create_file_init():
    with open('__init__.py', 'w', encoding='utf-8') as f:
        f.write('def save_to_json():\n  pass \n\n\n'
                'def find_roots():\n  pass \n\n\n'
                'def generate_csv_file():\n  pass')


create_file_init()

with open("__init__.py", "r") as init_file:
    code = init_file.read()

function_names = [
    "def save_to_json()",
    "def find_roots()",
    "def generate_csv_file()",
]

for func_name in function_names:
    if func_name not in code:
        print(f"Функция {func_name} не найдена в файле __init__.py")
    else:
        print(f"Функция {func_name} найдена в файле __init__.py")
