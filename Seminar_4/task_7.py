# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

names = ['stone', 'wanderer']
ages = [18, 34, 40]
sample = 'Пример'
s = 417
apple = 'Яблоко'


def change_name():
    new_vars = {}
    for var_name, var_value in globals().items():
        if var_name.endswith('s') and len(var_name) > 1:
            new_vars[var_name[:-1]] = var_value
            new_vars[var_name] = None
        else:
            new_vars[var_name] = var_value
    globals().update(new_vars)


change_name()

print(name)
print(age)
print(names)
print(ages)
print(sample)
print(s)