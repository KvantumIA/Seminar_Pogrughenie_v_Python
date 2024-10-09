# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

def mysort(lst, reverse=False):
    for j in range(len(lst)):
        for i in range(len(lst)-j-1):
            if reverse:
                if lst[i] < lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]
            else:
                if lst[i] > lst[i+1]:
                    lst[i], lst[i+1] = lst[i+1], lst[i]

lst = [4, 7, 2, 6, 3]

mysort(lst, reverse=True)
print(lst)