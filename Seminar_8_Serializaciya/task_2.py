# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json
import os

JSON_FILE_NAME = '../Seminar_13_Iscluchenia/Seminar/users.json'


def input_int(input_msg: str, error_msg: str, min_value: int = None, max_value: int = None):
    while True:
        number = input(input_msg)
        if number.isdigit():
            if min_value and max_value:
                if min_value <= int(number) <= max_value:
                    return int(number)
            else:
                return int(number)
        print(error_msg)


def get_user_id(id_list: list):
    while True:
        user_id = input_int('Введите ID: ', 'ID должен состоят из цифр!')
        if str(user_id) not in id_list:
            return user_id
        print('Такой ID уже зарегистрирован!')


def get_list_id(json_data):
    id_list = []
    for level, user in json_data.items():
        for user_id in user:
            id_list.append(str(user_id))
    return id_list


def json_load(file_name: str):
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='UTF-8') as json_file:
            return json.load(json_file)
    return {}


def json_write(file_name, json_data):
    with open(file_name, 'w', encoding='UTF-8') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)


def create_users():
    while True:
        user_data = json_load(JSON_FILE_NAME)
        id_list = get_list_id(user_data)
        if not (user_name := input('Введите имя пользователя: ')):
            print('Спасибо, ввод пользователей закончен')
            break
        user_id = get_user_id(id_list)
        user_level = input_int('Введите уровень доступа: ', 'Уровень должен быть от 1 до 7', 1, 7)
        if str(user_level) in user_data:
            user_data[str(user_level)][str(user_id)] = user_name
        else:
            user_data[str(user_level)] = {str(user_id): user_name}
        json_write(JSON_FILE_NAME, user_data)


if __name__ == '__main__':
    create_users()
