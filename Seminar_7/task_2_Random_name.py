# Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from string import ascii_lowercase
from random import choice, randint

MIN_LEN = 4
MAX_LEN = 7
# VOWELS = 'aeiou'
# CONSONANT = 'ABCDEFGHIKLMNOPQRSTVXYZ'.lower()
rus_alpha = {chr(i) for i in range(ord('а'), ord('я') + 1)}
VOWELS = ''.join({'а', 'у', 'е', 'ё', 'о', 'э', 'я', 'и', 'ю'})
CONSONANT = ''.join(rus_alpha.difference(VOWELS))


def random_name(min_len=MIN_LEN, max_len=MAX_LEN):
    name = ''
    for position in range(randint(min_len, max_len)):
        if position % 2:
            name += choice(VOWELS)
    else:
        name += choice(CONSONANT)
    # return name.capitalize()
    return 'test_file'


def fill_file(count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(count):
            f.write(random_name(MIN_LEN, MAX_LEN) + '\n')


if __name__ == '__main__':
    fill_file(10, 'names.txt')
