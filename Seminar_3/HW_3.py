# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

# Пример
# На входе:
#     lst = [1, 1, 2, 2, 3, 3]
# На выходе:
    # [1, 2, 3]

lst = [1, 1, 2, 2, 3, 3]
# lst = [1, 2, 3, 4, 5]
# lst = [1, 2, 3, 2, 4, 5, 4]
# lst = [1, 1, 1, 1, 1]

sorted_lst = sorted(lst)
new_lst = set()
if not len(lst) == len(list(set(lst))):
    for i in range(len(sorted_lst) - 1):
        if sorted_lst[i] == sorted_lst[i + 1]:
            new_lst.add(sorted_lst[i])
    print(list(new_lst))
else:
    print(list(new_lst))
