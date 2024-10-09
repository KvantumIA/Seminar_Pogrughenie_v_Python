"""
Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
"""
from string import ascii_letters

text = 'My string 7, правда'
text2 = 'New Number 98, заново'
text3 = 'test 732, правда'


def del_symbol(my_str: str):
    res = ''
    for i in my_str:
        if i in ascii_letters or i == ' ':
            res += i
    return res.lower()


if __name__ == '__main__':
    print(del_symbol('My string 7, правда'))

