# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.
my_list = ['qwearty','asadfg','zxcvab','uiop','hjkl','nmqwae','a12345','aaaaa','bcdfg']
my_new_list = []
for index, element in enumerate(my_list):
    my_new_list.append(element[::-1]) if (index % 2) == 1 else my_new_list.append(element)
print(my_new_list)
# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
my_new_list_2 = [element for element in my_list if element[0] == 'a']
print(my_new_list_2)
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
my_new_list_3 = [element for element in my_list if 'a' in element]
print(my_new_list_3)
# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Создать список и поместить туда имя самого молодого человека. Если возраст совпадает - поместить все имена самых молодых.
persons = [{"name": "John", "age": 26},
           {"name": "Jack", "age": 19},
           {"name": "Andrew", "age": 19},
           {"name": "Steve", "age": 23},
           {"name": "Peter", "age": 37},
           {"name": "Daniel", "age": 20}]
ages_of_persons = [age_value["age"] for age_value in persons]
youngest_persons = [person["name"] for person in persons if person.get("age") == min(ages_of_persons)]
print(youngest_persons)
# б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
names_of_persons_by_length = [len(name_value["name"]) for name_value in persons]
persons_with_longest_name = [person["name"] for person in persons if len(person["name"]) == max(names_of_persons_by_length)]
print(persons_with_longest_name)
# в) Посчитать среднее количество лет всех людей из начального списка.
sum_of_ages = 0
for person in persons:
    sum_of_ages += person.get('age')
average_age = sum_of_ages / len(persons)
print(average_age)
# 5) Даны два словаря my_dict_1 и my_dict_2.
my_dict_1 = {"a": 1,
             "b": 23,
             "c": 32,
             "d": 4,
             "e": 52,
             "f": 6}
my_dict_2 = {"x": 9,
             "c": 16,
             "b": 11,
             "s": 123,
             "e": 11,
             "k": 51}
# а) Создать список из ключей, которые есть в обоих словарях.
intersection_of_dicts = list(my_dict_1.keys() & my_dict_2.keys())
print(intersection_of_dicts)
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
unique_keys_of_dict_1 = my_dict_1.keys() - my_dict_2.keys()
print(unique_keys_of_dict_1)
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
new_dict = {element: my_dict_1[element] for element in my_dict_1 if element in unique_keys_of_dict_1}
print(new_dict)
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
new_dict_2 = dict(my_dict_1.items() | my_dict_2.items())
for key, value in new_dict_2.items():
    if key in intersection_of_dicts:
        new_dict_2.update({key: [my_dict_1[key], my_dict_2[key]]})
print(new_dict_2, my_dict_2)