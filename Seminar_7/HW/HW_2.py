# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
# Создайте файл __init__.py и запишите в него функцию rename_files
import os


def create_file_init():
    with open('__init__.py', 'w', encoding='utf-8') as f:
        f.write('def rename_files():\n  pass')

# def rename_files(desired_name, num_digits, source_ext, target_ext, path='test_folder'):
#     file_list = os.listdir(path)
#     os.chdir(path)
#     count = 1
#     for file in file_list:
#         extension = file.split('.')[1]
#         if count <= len(file_list):
#             if extension in source_ext:
#                 new_name = f'{desired_name}{str(count).zfill(num_digits)}.{target_ext}'
#                 os.rename(file, new_name)
#                 count += 1


create_file_init()
with open("__init__.py", "r") as init_file:
    code = init_file.read()

function_names = [
    "def rename_files"
]

for func_name in function_names:
    if func_name not in code:
        print(f"Функция {func_name} не найдена в файле __init__.py")
    else:
        print(f"Функция {func_name} найдена в файле __init__.py")