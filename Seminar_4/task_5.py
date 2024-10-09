# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def sum_slice(int_list: list[int], a_index: int, b_index: int) -> int:
    a_index, b_index = sorted([a_index, b_index])
    if a_index < 0:
        a_index = 0
    if b_index < 0:
        b_index = 1
    return sum(int_list[a_index:b_index + 1])


print(sum_slice([1, 2, 3, 4, 5, 6], -1, 2))