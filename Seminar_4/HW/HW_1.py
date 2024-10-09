# Напишите функцию для транспонирования матрицы transposed_matrix, принимает в аргументы matrix, и возвращает транспонированную матрицу.

# Пример использования На входе:
# matrix = [[1, 2, 3],
#          [4, 5, 6],
#          [7, 8, 9]]
# transposed_matrix = transpose(matrix)
# На выходе:
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# [] for _ in range(len(my_matrix))
def transpose(matrix):
    res = []

    data = list(zip(*matrix))
    for item in data:
        res.append(list(item))

    # for i in range(len(matrix[0])):
    #     temp = []
    #     for j in range(len(matrix)):
    #         temp.append(matrix[j][i])
    #     res.append(temp)
    return res


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
transposed_matrix = transpose(matrix)
print(transposed_matrix)

# print(transpose(matrix = [[1, 2], [3, 4]]))

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
# [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]

# matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
# [[1, 5], [2, 6], [3, 7], [4, 8]]
