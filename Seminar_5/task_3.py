# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

str1 = 'asdfsdfgfdgbfdbgf sdfgs dfg df'
itr = iter({letter: ord(letter) for letter in str1}.items())
for i in range(5):
    print(next(itr))