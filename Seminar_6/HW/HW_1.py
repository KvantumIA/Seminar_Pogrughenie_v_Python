# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем. На вход будет подаваться дата в формате "день.месяц.год".
# Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.
# Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в зависимости от результата проверки.
#
# Пример использования На входе:
# date_to_prove = 15.4.2023
# На выходе:
# True

# date_to_prove = '30.2.2024'
date_to_prove = '31.12.9999'

date_split = date_to_prove.split('.')

day = int(date_split[0])
month = int(date_split[1])
year = int(date_split[2])

if 1900 < year <= 9999:
    if 1 <= month <= 12:
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if 1 <= day <= 29:
                    print('True')
                else:
                    print('False')
            else:
                if 1 <= day <= 28:
                    print('True')
                else:
                    print('False')
        elif month % 2 != 0:
            if 1 <= day <= 30:
                print('True')
            else:
                print('False')
        else:
            if 1 <= day <= 31:
                print('True')
            else:
                print('False')
    else:
        print('False')
else:
    print('False')
