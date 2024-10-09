# ✔ Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def dict_text(numbers):
    a, b = sorted(list(map(int, numbers.split())))
    # my_dict = {}
    # for i in range(a, b + 1):
    #     my_dict[chr(i)] = i
    return {chr(i): i for i in range(a, b + 1)}


my_num = input("Введите цифры: ")
print(dict_text(my_num))
