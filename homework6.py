# Практическое задание по теме: "Словари и множества"

# Работа со словарями:
#   - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Например: Имя(str)-Год рождения(int).
#   - Выведите на экран словарь my_dict.
#   - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
#   - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
#  - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
#   - Выведите на экран словарь my_dict.
my_dict = {'Irina': 1985, 'Kosty': 1945, 'Misha': 2010, 'Slava': 2020, 'Olesy': 2018}   # словарь
print('Dict:', my_dict)                                     # вывод словаря в консоль
print('Existing value:', my_dict['Kosty'])                  # вывод значения ключа 'Kosty'
print('Not existing value:', my_dict.get('Marina Crazy'))   # вывод значения по отсутствующему ключу
my_dict.update({"Marina": 2006,
               "Sabrina": 2003})                            # добавление 2-х пар еще по такому же формату
a = my_dict.pop('Misha')                                    # удаление пары по существующему ключу
print('Deleted value:', a)                                  # вывод значения удаленного ключа
print('Modified dictionary:', my_dict)                      # Модифицированный словарь

# Работа с множествами:
#   - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
#   - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
#   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
#   - Удалите один любой элемент из множества my_set.
#   - Выведите на экран измененное множество my_set.
my_set = {1, 7, 0, False,  13, 23.134131646, 'Vasya', 0, False, 13, True, 7, 'Coffee', 'Mamka', 12, True, False }
#   множество из разных типов данных с повторяющимися значениями
print('Set:', my_set)                 # вывод множества
my_set.add('Vampir')                  # добавление уникального элемента в множество
my_set.add((1, 2, 3))                 # добавление уникального элемента в множество
my_set.discard('Coffee')              # удаление элемента в множестве
print('Modified set:', my_set)        # вывод множества
