# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии


def dict_salary(name, salary, bonus):
    # my_dict = {}
    # for i in range(len(name)):
    #     my_dict[name[i]] = salary[i] * float(bonus[i].replace('%', '')) / 100
    # return my_dict
    return {name[i]: salary[i] * float(bonus[i][:-1]) / 100 for i in range(len(name))}


my_name = ["Иван", "Владимир", "Сергей"]
my_salar = [1000, 2000, 3000]
my_bonus = ["10%", "12.2%", "11%"]
print(dict_salary(my_name, my_salar, my_bonus))
