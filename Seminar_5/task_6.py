# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def simple_numbers(count: int):
    yield 2
    cur_number = 3
    counter = 1
    while counter < count:
        for dev in range(3, int(cur_number ** 0.5) + 1, 2):
            if not cur_number % dev:
                break
        else:
            yield cur_number
            counter += 1
        cur_number += 2


for i in simple_numbers(10):
    print(i)