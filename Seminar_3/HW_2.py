# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов. Слова выведите в обратном алфавитном порядке.
#
# Пример
# На входе:
# text = 'Hello world. Hello Python. Hello again.'
# text = "Python 3.9 is the latest version of Python. It's awesome!"
text = 'Python is python, is, IS, and PYTHON.'

# На выходе:
# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]


sort_text = text.lower()
new_text = ''
for i in sort_text:
    if i in [".", "'", "-", "!", ","] or i.isdigit():
        new_text += " "
    else:
        new_text += i

words = new_text.split()

word_count = []
for i in set(words):
    count = 0
    temp = ()
    for j in words:
        if i == j:
            count += 1
        temp = i, count
    word_count.append(temp)

sorted_word_count = sorted(word_count, key=lambda x: (x[1], x[0]), reverse=True)

top_10 = sorted_word_count[:10]

print(top_10)

