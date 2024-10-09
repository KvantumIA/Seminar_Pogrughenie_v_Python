class MyException(Exception):
    """
    Классы ошибок
    """
    pass


class LevelError(MyException):
    def __init__(self, value):
        super().__init__(f'Пользователь не имеет нужного уровня доступа для '
                         f'добавления пользователя {value} с таким уровнем прав.')


class LoginError(MyException):
    def __init__(self, user_name, user_id):
        super().__init__(f'Ошибка входа. Пользователя с именем - {user_name} и '
                         f'ID - {user_id} не существует.')


class InputError(MyException):
    def __init__(self):
        super().__init__(f'Вы не ввели данные! Программа завершена.')
