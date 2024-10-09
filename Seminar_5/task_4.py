# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

# even_number_gen = (i for i in range(0, 101, 2) if sum(list(map(int, str(i)))) != 8)
even_number_gen = (i for i in range(0, 101, 2) if i // 10 + i % 10 != 8)

print(*even_number_gen)