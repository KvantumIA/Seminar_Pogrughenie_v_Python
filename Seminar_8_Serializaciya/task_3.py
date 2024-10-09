# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import json
import csv
import os


def json_load(file_name: str):
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='UTF-8') as json_file:
            return json.load(json_file)
    return {}


def convert_dict_to_list(json_data):
    csv_data = []
    for level, value in json_data.items():
        for id, user_name in value.items():
            csv_data.append([level, id, user_name])
    return csv_data


def write_csv(file_name, csv_data):
    with open(file_name, 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f, dialect='excel-tab')
        csv_write.writerows(csv_data)


def read_csv_dict(file_name):
    json_data = []
    with open(file_name, 'r', encoding='utf-8') as f:
        csv_dict = csv.DictReader(
            f, dialect='excel-tab')
        for line in csv_dict:
            json_data.append(line)
    return json_data


if __name__ == '__main__':
    json_data = json_load('../Seminar_13_Iscluchenia/Seminar/users.json')
    json1_data = read_csv_dict('json1.json')
    print(json_data)
    print()
    print(json1_data)
    csv_data = convert_dict_to_list(json_data)
    write_csv("csv_text.csv", csv_data)
