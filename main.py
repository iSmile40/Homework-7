from pprint import pprint
import os

# Задача 1

text = """Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г

Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт"""

with open("recipes.txt", "w", encoding='utf-8') as f:
    f.write(text)

cook_book = {}

with open('recipes.txt', encoding='utf-8') as f:
    for dish in f:
        dish_name = dish.strip()
        count = int(f.readline())
        ingredients_list = []
        for i in range(count):
            ingredients = f.readline().strip()
            splited = ingredients.split('|')
            ingredients_dict = dict()
            ingredients_dict['ingredient_name'] = splited[0]
            ingredients_dict['quantity'] = int(splited[1])
            ingredients_dict['measure'] = splited[2]
            ingredients_list.append(ingredients_dict)
        f.readline()
        cook_book[dish_name] = ingredients_list

print()
pprint(cook_book, width=100)

# Задача 2


def get_shop_list_by_dishes(dishes, person_count):
    recipe_dict = {}
    for dish_name in dishes:
        if dish_name in cook_book:
            for ingrs in cook_book[dish_name]:
                quantity_measure_dict = {}
                if ingrs['ingredient_name'] not in recipe_dict:
                    recipe_dict[ingrs['ingredient_name']] = quantity_measure_dict
                    quantity_measure_dict['quantity'] = ingrs['quantity'] * person_count
                    quantity_measure_dict['measure'] = ingrs['measure']
                else:
                    recipe_dict[ingrs['ingredient_name']]['quantity'] += ingrs['quantity'] * person_count
        else:
            print('Такого блюда нет')
    return recipe_dict

print()
pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))

# Задача 3

file_name = os.listdir('sorted')
result = []

for j in file_name:
    with open(f'sorted\{j}', encoding='utf-8') as f:
        lines = f.readlines()
        count = len(lines)
        result.append([j, count, ''.join(lines)])

result.sort(key=lambda x: x[1])

with open('result.txt', 'w', encoding='utf-8') as g:
    for item in result:
        g.write(f'{item[0]} \n')
        g.write(f'{item[1]} \n')
        g.write(f'{item[2]} {item[0]}')
