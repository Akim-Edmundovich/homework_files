import pprint

cook_book = {}
file_list = []

with open('recipes.txt', 'r') as f:
    for i in f:
        file_list.append(i.strip())

print(file_list)


def split_on(what, splitter=''):  # Формирует список списков ингредиентов из файла. Разделитель - пустая строка.
    splitted = [[]]
    for item in what:
        if item == splitter:
            splitted.append([])
        else:
            splitted[-1].append(item)

    return splitted


split_list = split_on(file_list)

for i in split_list:  # Разбивает строки с "|"
    for item in range(2, len(i)):
        i[item] = i[item].split('|')

for i in split_list:  # Формирует словарь с блюдами и нужным кол-вом ингредиентов
    cook_book[i[0]] = []
    for k in range(2, len(i)):
        cook_book[i[0]].append({'ingredient_name': i[k][0], 'quantity': int(i[k][1]) * int(i[1]), 'measure': i[k][2]})

# pprint.pp(cook_book)
