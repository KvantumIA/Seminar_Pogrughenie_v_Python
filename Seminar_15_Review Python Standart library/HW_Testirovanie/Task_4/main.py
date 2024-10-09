import argparse


def new_parser():
    parser = argparse.ArgumentParser(description='Новый парсер')
    parser.add_argument('text', type=str, help='Аргумент принимающий текст')
    parser.add_argument('number', type=int, help='Аргумент принимающий цифры')

    parser.add_argument('-v', '--verbose', action='store_true', help='Вывод дополнительной информации')
    parser.add_argument('-r', '--repeat', type=int, default=1, help='Количество повторений строки')

    args = parser.parse_args()

    if args.verbose:
        print(f'Полученные аргументы: number={args.number}, text = "{args.text}", repeat = {args.repeat}')

    print(f'Число: {args.number}, Строка: {args.text * args.repeat}')


if __name__ == '__main__':
    new_parser()