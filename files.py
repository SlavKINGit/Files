print()
print('TASK 1')
print()

with open('recipes.txt', encoding='utf8') as recipes:
    cook_book = {}
    for i in recipes:
        dish_name = i.strip()
        cook_book[f'{dish_name}'] = []
        quantity_of_ingredients = recipes.readline()
        for j in range(int(quantity_of_ingredients)):
            read_line = recipes.readline()
            ingredient_name, quantity, measure = read_line.split(' | ')
            description_of_ingridients = {'ingredient_name' : ingredient_name, 'quantity' : int(quantity), 'measure' : measure.strip()}
            cook_book[f'{dish_name}'].append(description_of_ingridients)
        recipes.readline()
    print(cook_book)

print()
print('-'*50)
print()

print('TASK 2')
print()

total_order = {}
def get_shop_list_by_dishes(dishes, person_count):
    for i in dishes:
        for j in cook_book[i]:
            for k, v in j.items():
                name = j['ingredient_name']
                measure = j['measure']
                quantity = j['quantity']
                total_order[f'{name}'] = {'measure' : f'{measure}', 'quantity' : f'{quantity*person_count}'}
    print(total_order)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

print()
print('-'*50)
print()

print('TASK 3')
print()

with open('1.txt', encoding='utf8') as file1, open('2.txt', encoding='utf8') as file2, open('3.txt', encoding='utf8') as file3, open('total.txt', 'w', encoding='utf8') as file4:
    files = [file1, file2, file3]
    my_list = []
    counter = 1
    for i in files:
        z = i.read()
        x = z.count('\n')+1
        new_list = [x, f'{counter}.txt', f'{z}']
        my_list.append(new_list)
        counter += 1
    my_list.sort()
    for i in my_list:
        file4.write(f'{i[1]}\n')
        file4.write(f'{str(i[0])}\n')
        file4.write(f'{i[2]}\n')
        # print(f'{i[1]}\n')
        # print(f'{str(i[0])}\n')
        # print(f'{i[2]}\n')

# print()
# print('Вот эти данные сохранились в отдельный файл')