# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
#
# Пример использования.
# На входе:
# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# print(params)
# На выходе:
# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}

def key_params(**kwargs):
    variables = {}

    for name, value in kwargs.items():
        if isinstance(value, dict) and len(value) != 0:
            variables_value = {}
            for name_value, value_value in value.items():
                variables_value[str(name_value)] = value_value
            variables[str(variables_value)] = name
        elif isinstance(value, list) or isinstance(value, set) or isinstance(value, dict):
            variables[str(value)] = name
        else:
            variables[value] = name
    return variables


# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}

# params = key_params(a = 42, b='hello', c=3.14, d='world')
# # {42: 'a', 'hello': 'b', 3.14: 'c', 'world': 'd'}

# params = key_params(a=None, b='', c=[], d={})
# # {None: 'a', '': 'b', '[]': 'c', '{}': 'd'}

# params = key_params(a = 42, b = 'hello', c = 3.14, d = 'world')
# # {42: 'a', 'hello': 'b', 3.14: 'c', 'world': 'd'}

# params = key_params(a = True, b = False, c = True, d = False)
# # {True: 'c', False: 'd'}

# params = key_params(name = 'Alice', age = 30, scores = [85, 90, 78], info = {'city': 'New York', 'email': 'alice@example.com'})
# # {'Alice': 'name', 30: 'age', '[85, 90, 78]': 'scores', "{'city': 'New York', 'email': 'alice@example.com'}": 'info'}

print(params)
