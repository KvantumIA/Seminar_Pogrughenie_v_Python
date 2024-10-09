"""
На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging.
"""

import logging

FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
         'в строке {lineno:03d} функция "{funcName}()" ' \
         'в {created} секунд записала сообщение: {msg}'

logger = logging.getLogger(__name__)
logging.basicConfig(filename='log.txt', filemode='w', encoding='utf-8',
                    level=logging.INFO)


def dec_logger(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        logger_text = f'{func.__name__}:{result}, args:{args}, {kwargs}'
        logger.info(logger_text)
        return result

    return inner


@dec_logger
def devision(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError as e:
        logger.error(e)


print(devision(4, 2))
print(devision(4, 0))
