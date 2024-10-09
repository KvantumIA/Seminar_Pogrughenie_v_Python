# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def text_list(text: str):
    # res = set()
    # for i in text:
    #     res.add(ord(i))
    # return sorted(res, reverse=True)
    return sorted([ord(i) for i in set(text)], reverse=True)


in_text = input("Введите текст: ")

print(text_list(in_text))
