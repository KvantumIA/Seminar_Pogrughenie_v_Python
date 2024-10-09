# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
#
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории
#
# Пример использования.
# На входе:
# rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")

# На выходе:
# new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc, new_file_003.doc, new_file_002.doc,
# new_file_009.doc, new_file_010.doc

import os
import shutil


def rename_files(desired_name, num_digits, source_ext, target_ext, path='test_folder'):
    file_list = os.listdir(path)
    os.chdir(path)
    count = 1
    for file in file_list:
        extension = file.split('.')[1]
        if count <= len(file_list):
            if extension in source_ext:
                new_name = f'{desired_name}{str(count).zfill(num_digits)}.{target_ext}'
                os.rename(file, new_name)
                count += 1


def create_file():
    # Создать тестовую папку
    folder_name = "test_folder"
    folder_path = os.path.join(os.getcwd(), folder_name)
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)

    # Заполнить тестовую папку
    for i in range(10):
        file_name = f"test{i}.txt"
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, "w") as file:
            file.write("This is a test file.\n")
            file.close()

    file_name = "test.doc"
    file_path = os.path.join(folder_path, file_name)

    with open(file_path, "w") as file:
        file.write("This is a test file.\n")
        file.close()


if __name__ == '__main__':
    # create_file()

    # rename_files(desired_name="file_", num_digits=4, source_ext="txt", target_ext="txt")
    # file_0001.txt

    rename_files(desired_name="file_", num_digits=4, source_ext="txt", target_ext="txt")
    # пустота

    # rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
    # new_file_001.doc, new_file_002.doc, new_file_003.doc, new_file_004.doc, new_file_005.doc, new_file_006.doc,
    # new_file_007.doc, new_file_008.doc, new_file_009.doc, new_file_010.doc, test.doc
