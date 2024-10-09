import logging
import os


class MyLogging:
    """
    Класс для ведения лога программы
    """
    def __init__(self):
        self.start_logger()

    @staticmethod
    def start_logger():
        FORMAT = '{levelname:<8} - {asctime}. В модуле "{module_name}" ' \
                 'в строке {lineno:03d} функция "{funcName}()" ' \
                 'в {created} секунд записала сообщение: {msg}'
        logger = logging.getLogger(__name__)
        log_file_path = os.path.join(os.path.dirname(__file__),
                                     '../Documents/log.log')
        logging.basicConfig(filename=log_file_path, filemode='a', encoding='utf-8',
                            level=logging.INFO, format=FORMAT, style="{")
        return logger