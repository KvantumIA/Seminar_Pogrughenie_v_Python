from typing import Callable


def how_are_you(func: Callable):
    def wrapper(*args, **kwargs):
        text = input("Как дела? Ответ: ")
        print("А у меня не очень! Ладно, держи свою функцию.")
        res = func(*args, **kwargs)
        return res
    return wrapper


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()
