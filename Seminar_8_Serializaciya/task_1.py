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


def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as f:
        text = f.readlines()
    text_dict = {}
    for item in text:
        key, value = item.strip().split(' | ')
        key = key.title()
        if key in text_dict:
            text_dict[key].append(value)
        else:
            text_dict[key] = [value]
    return text_dict


def write_json(file_name, json_data):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)


json_data = read_file('names_mult.txt')
write_json('../Seminar_13_Iscluchenia/Seminar/users.json', json_data)
