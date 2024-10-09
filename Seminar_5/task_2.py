# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

my_str = "from zero to hero"
my_dict = {i: ord(i) for i in my_str if i.isalpha()}
print(my_dict)

print({i: ord(i) for i in set(input('Введите строку: ').replace(' ', ''))})

