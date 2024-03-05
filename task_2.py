# coding: utf8

cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
}

cook_dict = {}


def get_shop_list_by_dishes(dishes: list, person_count):
    '''Создает словарь с ингредиентами'''
    for i in dishes:
        for dish in cook_book[i]:
            if dish['ingredient_name'] not in cook_dict:
                cook_dict[dish['ingredient_name']] = {'measure': dish['measure'],
                                                      'quantity': dish['quantity'] * person_count}
            else:  # Если игредиенты повторяются
                cook_dict[dish['ingredient_name']] = {'measure': dish['measure'],
                                                      'quantity': dish['quantity'] * person_count + dish[
                                                          'quantity'] * person_count}

    return cook_dict


print(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель', 'Запеченный картофель'], 3))
