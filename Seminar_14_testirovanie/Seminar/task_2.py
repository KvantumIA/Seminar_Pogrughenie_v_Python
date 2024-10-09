"""
Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
"""

import doctest
from string import ascii_letters

text_original = 'my string'
text_upper = 'My String'
text_punctuation = 'my, string!'
text_foreign = 'my stringмоястрока'
text_all = 'My String_моя_строка!'


def del_symbol(my_str: str):
    """
    >>> del_symbol(text_original) == text_original
    True
    >>> del_symbol(text_upper) == text_original
    True
    >>> del_symbol(text_punctuation) == text_original
    True
    >>> del_symbol(text_foreign) == text_original
    True
    >>> del_symbol(text_all) == text_original
    True
    """
    res = ''
    for i in my_str:
        if i in ascii_letters or i == ' ':
            res += i
    return res.lower()


if __name__ == '__main__':
    doctest.testmod(verbose=True)

