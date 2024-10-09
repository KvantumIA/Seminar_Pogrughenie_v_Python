# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

import json
import csv
import os


def json_load(file_name: str):
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='UTF-8') as json_file:
            return json.load(json_file)
    return {}


def read_csv(file_name):
    csv_data = []
    with open(file_name, 'r', newline='', encoding='utf-8') as f:
        for line in csv.reader(f, dialect='excel-tab'):
            csv_data.append(line)
    return csv_data


def convert_csv_data(csv_data):
    for item in csv_data:
        item[1] = item[1].zfill(10)
        item.append(hash(item[1] + item[2]))
    return {item[-1]: item[:-1] for item in csv_data}


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
    csv_data = read_csv('../Seminar_13_Iscluchenia/Seminar/users.json')
   