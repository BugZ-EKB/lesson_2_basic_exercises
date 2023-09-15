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
name_dict = {}
for student in students:
    if student['first_name'] not in name_dict:
        name_dict[student['first_name']] = 1
    else:
        name_dict[student['first_name']] += 1

for k, v in name_dict.items():
    print(f'{k}: {v}')
print()


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

name_dict = {}
for student in students:
    if student['first_name'] not in name_dict:
        name_dict[student['first_name']] = 1
    else:
        name_dict[student['first_name']] += 1

max_val = max(name_dict.values())
for k, v in name_dict.items():
    if v == max_val:
        print(f'Самое частое имя среди учеников: {k}')
print()

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
def max_number_in_class(class_dict):
    name_dict = {}
    for student in class_dict:
        if student['first_name'] not in name_dict:
            name_dict[student['first_name']] = 1
        else:
            name_dict[student['first_name']] += 1
    max_val = max(name_dict.values())
    for k, v in name_dict.items():
        if v == max_val:
            return k


group_number = 1
for students in school_students:
    max_name = max_number_in_class(students)
    print(f'Самое частое имя в классе {group_number}: {max_name}')
    group_number += 1
print()

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


def gender_structure(class_dict):
    gender_dict = {'девочки': 0, 'мальчики': 0}
    for student in class_dict:
        if is_male[student['first_name']]:
            gender_dict['мальчики'] += 1
        else:
            gender_dict['девочки'] += 1
    return gender_dict


def total_structure(school_class):
    for cl in school_class:
        total = gender_structure(cl['students'])
        print(f'Класс {cl["class"]}: девочки {total["девочки"]}, мальчики {total["мальчики"]} ')


total_structure(school)
print()


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
def gender_structure(class_dict):
    gender_dict = {'девочки': 0, 'мальчики': 0}
    for student in class_dict:
        if is_male[student['first_name']]:
            gender_dict['мальчики'] += 1
        else:
            gender_dict['девочки'] += 1
    return gender_dict


def total_structure(school_class):
    gender_max = {'male': 0, 'female': 0, 'male_class': '', 'female_class': ''}
    for cl in school_class:
        total = gender_structure(cl['students'])
        if total["девочки"] > gender_max['female']:
            gender_max['female'] = total["девочки"]
            gender_max['female_class'] = cl['class']
        if total["мальчики"] > gender_max['male']:
            gender_max['male'] = total["мальчики"]
            gender_max['male_class'] = cl['class']
    print(f'Больше всего мальчиков в классе {gender_max["male_class"]} ')
    print(f'Больше всего девочек в классе {gender_max["female_class"]} ')


total_structure(school)

