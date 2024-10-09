"""Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения."""



def error_func():
    while True:
        try:
            user_input = input('Type a number: ')
            return int(user_input)
        except ValueError:
            try:
                return float(user_input)
            except ValueError:
                print('Надо ввести инт или флоат')


a = error_func()
print(a)