# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

# Пример
# На входе:
    # num = 255
# На выходе:
    # Шестнадцатеричное представление числа: FF
    # Проверка результата: 0xff

# def to_hex(num):
#     if num < 0:
#         raise ValueError("Отрицательные числа не могут быть представлены в шестнадцатеричной системе")
#
#     hex_chars = "0123456789ABCDEF"
#     hex_string = ""
#
#     while num > 0:
#         remainder = num % 16
#         hex_string = hex_chars[remainder] + hex_string
#         num //= 16
#
#     return hex_string if hex_string else "0"
#
#
# # Пример использования
# num = int(input("Введите целое число: "))
# hexadecimal = to_hex(num)
# print("Шестнадцатеричное представление:", hexadecimal)
#
# # Проверка с использованием встроенной функции hex()
# print("Проверка с использованием встроенной функции hex():", hex(num))


num = 65535
hex_exam = hex(num)
hex_chars = "0123456789ABCDEF"
hex_string = ""

while num > 0:
    remainder = num % 16
    hex_string = hex_chars[remainder] + hex_string
    num //= 16

if num < 0:
    raise ValueError("Отрицательные числа не могут быть представлены в шестнадцатеричной системе")
else:
    print("Шестнадцатеричное представление числа:", hex_string)
    print("Проверка результата:", hex_exam)
