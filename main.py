import os
current = os.getcwd()
folder_name = 'Recipies'
file_name = 'recipies.txt'
full_path = os.path.join(current, folder_name, file_name)
cook_book = {}
with open(full_path, 'rt', encoding='utf-8') as file:
    for i in file:
        dish_name = i.strip()
        cook = {dish_name: []}
        ingredients_count = file.readline()
        for i in range(int(ingredients_count)):
            ingr = file.readline()
            ingredient_name, quantity, measure = ingr.strip().split(' | ')
            cook[dish_name].append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        for i in cook:
            cook_book[dish_name] = cook[dish_name]
        blank_line = file.readline()
print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop = {}
    for j in dishes:
        for j in cook_book.get(j):
            shop_dict = {j['ingredient_name']: {'measure': j['measure'], 'quantity': int(j['quantity']) * person_count}}
            for key, value in shop_dict.items():
                shop[key] = shop_dict[key]
    return print(shop)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

files_list = ['1.txt', '2.txt', '3.txt']
sorted_dict = {}
for file in files_list:
    string_count_dict = {file: (sum(1 for line in open(file, 'rt', encoding='utf-8')))}
    for key, value in string_count_dict.items():
        sorted_dict[key] = string_count_dict[key]
sorted_string_count_list = sorted(sorted_dict.items(), key=lambda x: x[1])
for i in sorted_string_count_list:
    with open(i[0], 'rt', encoding='utf-8') as file:
        strings_list = file.readlines()
    with open('final.txt', 'a', encoding='utf-8') as final_file:
        final_file.writelines(f'{i[0]}\n')
        final_file.writelines(f'{i[1]}\n')
        final_file.writelines(strings_list)
        final_file.writelines('\n')