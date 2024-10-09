from Company import Company
from MyException import InputError
from Logging import MyLogging
import argparse


class Start:
    """
    Класс отвечающий за начало программы.
    """

    def __init__(self):
        self.logger = MyLogging().start_logger()
        self.company = Company()
        try:
            parser = argparse.ArgumentParser(
                description='Авторизация и регистрация нового пользователя.')
            parser.add_argument('--name', type=str, default='Сергей',
                                help='Введите имя пользователя')
            parser.add_argument('--id', type=str, help='Введите ID')
            parser.add_argument('--verbose', action='store_true',
                                help='Выводить подробную информацию')
            parser.add_argument('--name_new_user', type=str,
                                help='Введите имя нового пользователя')
            parser.add_argument('--id_new_user', type=int,
                                help='Введите ID нового пользователя')
            parser.add_argument('--level_new_user', type=int,
                                help='Введите уровень нового пользователя')
            args = parser.parse_args()
            self.start(args)
        except InputError as e:
            self.logger.error(e, extra={'module_name': __name__})

    def start(self, args):
        """
        Отвечает за старт программы.
        """
        print('Начало программы. Пожалуйста авторизуйтесь.')

        args.name = input("Введите ваше имя: ")
        args.id = input("Введите ваш ID: ")

        user_level = self.company.login(args.id, args.name)

        if user_level:
            args.name_new_user = input("Введите имя нового пользователя: ")
            args.id_new_user = int(
                input("Введите ID нового пользователя: "))
            args.level_new_user = int(
                input("Введите уровень нового пользователя: "))
            self.company.add_user(args.id_new_user, args.name_new_user,
                                  args.level_new_user)
        else:
            raise InputError()


if __name__ == '__main__':
    company = Company()
    company.login('17', 'Сергей')
    print(company.authorised_user)
    company.add_user('14', 'Светлана', 5)
    print(company.user_set)
