# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
# Для проверки своего кода используйте модуль fractions.
from fractions import Fraction

# Пример
# На входе:
    # frac1 = "1/2"
    # frac2 = "1/3"
# На выходе:
    # Сумма дробей: 5/6
    # Произведение дробей: 1/6
    # Сумма дробей: 5/6
    # Произведение дробей: 1/6

frac1 = "1/2"
frac2 = "1/3"


def add_fractions(frac1, frac2):
    # Разделяем дроби на числитель и знаменатель
    num1, denom1 = map(int, frac1.split('/'))
    num2, denom2 = map(int, frac2.split('/'))

    # Находим общий знаменатель
    common_denom = denom1 * denom2

    # Вычисляем числитель суммы
    sum_num = num1 * denom2 + num2 * denom1

    # Возвращаем строку суммы
    return f"{sum_num}/{common_denom}"


def multiply_fractions(frac1, frac2):
    # Разделяем дроби на числитель и знаменатель
    num1, denom1 = map(int, frac1.split('/'))
    num2, denom2 = map(int, frac2.split('/'))

    # Вычисляем числитель произведения
    product_num = num1 * num2

    # Вычисляем знаменатель произведения
    product_denom = denom1 * denom2

    # Возвращаем строку произведения
    return f"{product_num}/{product_denom}"


def check_fractions(frac1, frac2):
    num1, denom1 = map(int, frac1.split('/'))
    num2, denom2 = map(int, frac2.split('/'))
    fraction1 = Fraction(num1, denom1)
    fraction2 = Fraction(num2, denom2)

    # Считаем сумму и произведение дробей
    sum_fraction_check = fraction1 + fraction2
    product_fraction_check = fraction1 * fraction2

    return sum_fraction_check, product_fraction_check


sum_result = add_fractions(frac1, frac2)
product_result = multiply_fractions(frac1, frac2)

print("Сумма дробей:", sum_result)
print("Произведение дробей:", product_result)

sum_fraction_check, product_fraction_check = check_fractions(frac1, frac2)
print("Сумма дробей:", sum_fraction_check)
print("Произведение дробей:", product_fraction_check)
