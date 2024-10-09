# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите
# 4 успешных расстановки.
# Под "успешной расстановкой ферзей" в данном контексте подразумевается такая расстановка ферзей на шахматной доске, в которой ни один ферзь не
# бьет другого.
# Другими словами, ферзи размещены таким образом, что они не находятся на одной вертикали, горизонтали или диагонали.
#
# Список из 4х комбинаций координат сохраните в board_list. Дополнительно печатать его не надо.
#
# Пример использования На входе:
# print(generate_boards())

# На выходе:
# [[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)], [(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)], [(1, 3), (2, 6), (3, 8), (4, 2),
# (5, 4), (6, 1), (7, 7), (8, 5)], [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]]


import random


def check_queens(queens):
    for i in range(len(queens)):
        queen_one = queens[i]
        for queen_next in queens:
            if queen_one != queen_next:
                if queen_one[0] == queen_next[0] or queen_one[1] == queen_next[1]:
                    return True
            for count in range(1, 9):
                if 0 < queen_one[0] - count < 9 and 0 < queen_one[1] - count < 9:
                    if queen_one[0] != queen_next[0] and queen_one[1] != queen_next[1]:
                        if queen_next[0] == queen_one[0] - count and queen_next[1] == queen_one[1] - count:
                            return True
    else:
        return False


def gen_one_board():
    board = []
    columns = list(range(1, 9))
    random.shuffle(columns)
    for row in range(1, 9):
        board.append((row, columns[row - 1]))
    return board


def generate_boards():
    board_result = []
    i = 0
    while i < 4:
        new_board = gen_one_board()
        while not check_queens(new_board):
            new_board = gen_one_board()
        board_result.append(new_board)
        i += 1
    return board_result


print(generate_boards())

