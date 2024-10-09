# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
# функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и check_queens(queens), которая проверяет
# все возможные пары ферзей.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка
# 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют
# друг друга верните
# истину, а если бьют - ложь. Не забудьте напечатать результат.
#
# Пример использования.
# На входе:
# queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
# На выходе:
# False


# def check_queens(queens):
#     for i in range(len(queens)):
#         queen_one = queens[i]
#         for queen_next in queens:
#             if queen_one != queen_next:
#                 if queen_one[0] == queen_next[0] or queen_one[1] == queen_next[1]:
#                     return 'False'
#             for count in range(1, 9):
#                 if 0 < queen_one[0] - count < 9 and 0 < queen_one[1] - count < 9:
#                     if queen_one[0] != queen_next[0] and queen_one[1] != queen_next[1]:
#                         if queen_next[0] == queen_one[0] - count and queen_next[1] == queen_one[1] - count:
#                             return 'False'
#     else:
#         return 'True'
def check_queens(queens):
    n = len(queens)
    for i in range(n):
        for j in range(i + 1, n):
            q1 = queens[i]
            q2 = queens[j]
            if q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
                return False
    return True

queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
# queens = [(6, 5), (7, 8), (3, 8), (1, 3), (1, 8), (4, 5), (6, 2), (5, 3)]
# queens = [(1, 1), (2, 3)]
print(check_queens(queens))
