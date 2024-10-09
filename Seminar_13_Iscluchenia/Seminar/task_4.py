"""Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей."""
import json


class User:
    def __init__(self, user_id, name, level):
        self.id = user_id
        self.name = name
        self.level = level

    def __repr__(self):
        return f'{self.name} ({self.id}, {self.level})'


class Company:
    def __init__(self):
        self.user_list = []
        self.path = "users.json"
        self.reade_json_file()

    def reade_json_file(self):
        with open(self.path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        for level, user in json_data.items():
            for user_id, user_name in user.items():
                self.user_list.append(User(user_id, user_name, level))


if __name__ == '__main__':
    company = Company()
    print(company.user_list)
