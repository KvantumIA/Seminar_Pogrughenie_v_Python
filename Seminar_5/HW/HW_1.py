# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Пример использования.
# На входе:
# file_path = "C:/Users/User/Documents/example.txt"
#
# На выходе:
# ('C:/Users/User/Documents/', 'example', '.txt')

def get_file_info(file_path):
    file_split = file_path.rsplit('/', 1)
    file_absolute_path = file_split[0]
    file_name = file_split[-1].rsplit('.', 1)
    if len(file_split) > 1:
        return f"{file_absolute_path}/", file_name[0], f'.{file_name[-1]}'
    else:
        return '', file_name[0], f'.{file_name[-1]}'


print(get_file_info(file_path='C:/Users/User/Documents/example.txt'))
print(get_file_info(file_path='/home/user/data/file.py'))
print(get_file_info(file_path='C:/Projects/project1/code/script.py'))
print(get_file_info(file_path='/home/user/docs/my.file.with.dots.txt'))
print(get_file_info(file_path = 'file_in_current_directory.txt'))
