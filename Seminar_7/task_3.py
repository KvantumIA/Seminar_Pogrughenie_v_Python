# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        return list(map(lambda x: x.strip(), f.readlines()))


def write_file(names, numbers, file_name):
    max_len = len(max(names, numbers, key=len))
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(max_len):
            num1, num2 = map(float, numbers[i % len(numbers)].split('|'))
            if (multiple := num1 * num2) < 0:
                f.write(f'{names[i % len(names)].lower()} | {abs(multiple)}\n')
            else:
                f.write(f'{names[i % len(names)].upper()} | {int(multiple)}\n')


names = read_file('names.txt')
numbers = read_file('test.txt')

if __name__ == '__main__':
    write_file(names, numbers, 'names_mult.txt')
