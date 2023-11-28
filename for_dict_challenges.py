# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
name_dict = dict()

for el in students:
    if el['first_name'] not in name_dict:
        name_dict[el['first_name']] = 1
    else:
        name_dict[el['first_name']] += 1

for key, value in name_dict.items():
    print(key, value)


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
name_dict = dict()

for el in students:
    if el['first_name'] not in name_dict:
        name_dict[el['first_name']] = 1
    else:
        name_dict[el['first_name']] += 1

max_ = max(name_dict, key=name_dict.get)
print(f'Самое частое имя среди учеников: {max_}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for class_name in school_students:
    my_dict = {}
    for element in class_name:
        if element['first_name'] not in my_dict:
            my_dict[element['first_name']] = 1
        else:
            my_dict[element['first_name']] += 1
    max_name = max(my_dict, key=my_dict.get)
    print(f'Самое частое имя в классе {school_students.index(class_name)+1}: {max_name}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for class_ in school:
    male_count = 0
    female_count = 0
    for student in class_['students']:
        if student['first_name'] in is_male:
            if is_male[student['first_name']] is True:
                male_count += 1
            else:
                female_count += 1
        else:
            print('Not found')

    print(f'Класс {class_["class"]}: девочки {female_count}, мальчики {male_count}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

my_lst = []
for class_ in school:
    male_count = 0
    female_count = 0
    dict_male = {}
    for student in class_['students']:
        if student['first_name'] in is_male:
            if is_male[student['first_name']] is True:
                male_count += 1
            else:
                female_count += 1
        else:
            continue
        dict_male[class_['class']] = {'girls': female_count, 'boys': male_count}

    my_lst.append(dict_male)

for key in my_lst:
    for key, value in key.items():
        if value['boys'] > value['girls']:
            print(f'Больше всего мальчиков в классе {key}')
        else:
            print(f'Больше всего девочек в классе {key}')

