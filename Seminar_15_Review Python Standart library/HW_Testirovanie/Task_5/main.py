import argparse
import logging
import os


def read_dir(path_dir):
    log = logging.getLogger('HW')
    logging.basicConfig(filename='file_info.txt', filemode='w',
                        encoding='utf-8', level=logging.INFO, style="{")
    if os.path.isdir(path_dir):
        for address, dirs, files in os.walk(path_dir):

            for name_files in files:
                temp = dict()
                name_file = os.path.splitext(name_files)
                temp['Name'] = name_file[0]
                temp['Extension'] = name_file[1].split('.')[1]
                temp['Path'] = address
                log.info(temp)

            for name_dir in dirs:
                temp = dict()
                temp['Name'] = name_dir
                temp['Path'] =address
                log.info(temp)
    print('Работа парсера закончена, проверьте файл в корневой папке: file_info.txt')


def parser_dir():
    parser = argparse.ArgumentParser(description='Новый парсер для считывания '
                                                 'данных в папке')
    parser.add_argument('path', type=str,
                        help='Укажите путь до папки', default='test')
    args = parser.parse_args()
    read_dir(args.path)


if __name__ == '__main__':
    parser_dir()
