import json
from MyException import LoginError, LevelError
from Logging import MyLogging
from User import User
import os


class Company:
    """
    Класс отвечающий за авторизацию и создание нового пользователя.
    """

    def __init__(self):
        self.logger = MyLogging().start_logger()
        self.user_set = set()
        self.path = os.path.join(os.path.dirname(__file__),
                                 '../Documents/users.json')
        self.reade_json_file()

    def reade_json_file(self):
        """
        Функция для чтения JSON файла с зарегистрированными пользователями
        :return: Возвращает словарь с пользователями
        """
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
            for level, user in json_data.items():
                for user_id, user_name in user.items():
                    self.user_set.add(User(user_id, user_name, level))
            self.logger.info("Файл успешно прочитан.",
                             extra={'module_name': __name__})
        except PermissionError as e:
            self.logger.error(e, extra={'module_name': __name__})

    def login(self, user_id, user_name):
        """
        Авторизация пользователя в системе.
        :param user_id: номер ID пользователя
        :param user_name: имя пользователя
        :return: Возвращает уровень доступа для добавления нового пользователя
        """
        self.logger.info('Авторизация пользователя',
                         extra={'module_name': __name__})
        login_user = User(user_id, user_name, 0)

        count = len(self.user_set)

        for user in self.user_set:
            if count > 0:
                if user == login_user:
                    print("Авторизация прошла успешно!")
                    self.logger.info(
                        f"Авторизация пользователя, {user_name} c user_ID = {user_id}, прошла успешно!",
                        extra={'module_name': __name__})
                    self.authorised_user = user
                    return user.level
                else:
                    count -= 1
        else:
            self.logger.error(
                f'Ошибка входа. Пользователя с именем - {user_name} и ID - {user_id} не существует.',
                extra={'module_name': __name__})
            raise LoginError(user_name, user_id)

    def add_user(self, user_id, user_name, level):
        """
        Функция для добавления нового пользователя в систему
        :param user_id: ID нового пользователя
        :param user_name: Имя нового пользователя
        :param level: Необходимый уровень доступа для создания пользователя,
        вычисляется при авторизации
        :return: Записывает нового пользователя в систему
        """
        self.logger.info('Добавление нового пользователя',
                         extra={'module_name': __name__})
        if int(self.authorised_user.level) > level:
            self.logger.error(
                f'Пользователь не имеет нужного уровня доступа для '
                f'добавления пользователя {user_name} с таким уровнем'
                f' прав.', extra={'module_name': __name__})
            raise LevelError
        new_user = User(user_id, user_name, level)
        print(f"Пользователь {user_name} добавлен в базу пользователей")
        self.logger.info(
            f"Пользователь {user_name} добавлен в базу пользователей",
            extra={'module_name': __name__})
        self.user_set.add(new_user)
