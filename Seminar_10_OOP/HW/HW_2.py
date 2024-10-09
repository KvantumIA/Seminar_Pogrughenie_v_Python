"""На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
Первый список ваш лотерейный билет.
Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.

Напишите класс LotteryGame, который будет иметь метод compare_lists, который будет сравнивать числа из вашего билета из list1 со списком выпавших чисел list2

Если совпадающих чисел нет, то выведите на экран:
Совпадающих чисел нет.

Пример входных данных:
list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()


Пример выходных данных:
Совпадающие числа: [3, 12, 8, 41, 9, 14, 5]
Количество совпадающих чисел: 7"""


class LotteryGame:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    # def compare_lists(self):
    #     res = []
    #     for i in self.list_1:
    #         for j in self.list_2:
    #             if i == j:
    #                 if len(res) < len(self.list_1):
    #                     res.append(i)
    #     if res:
    #         print(f'Совпадающие числа: {res}\nКоличество совпадающих чисел: {len(res)}')
    #     else:
    #         print(f'Совпадающих чисел нет.')

    def compare_lists(self):
        matching_numbers = set(self.list_1) & set(self.list_2)
        if not matching_numbers:
            print("Совпадающих чисел нет.")
        else:
            print("Совпадающие числа:", list(matching_numbers))
            print("Количество совпадающих чисел:", len(matching_numbers))
            return matching_numbers


list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]
# list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()

