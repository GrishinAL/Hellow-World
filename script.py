if 43 > 42:
    print('yes bitch... 43 is fucking bigger then 42')

# Присваиваем переменной значение списка и выводим
cast = ["Cleese", 'Palin', 'Jones', "Idle"]
print(cast)
# Считаем и выводим кол-во элементов списка
print(len(cast))
# Выводим 1 элемент списка (начинается с 0)
print(cast[1])

# Добавить 1 элемент в конец списка - метод append()
cast.append('Gilliam')
# Добавить несколько элементов в конец списка
cast.extend(["Gilliam", "Chapman"])
# Добавить элемент на определенную позицию
cast.insert(0, "Chapman")

# Удалить последний элемент списка
cast.pop()
# Удалить конкретный элемент списка (по номеру)
cast.pop(1)
# Удалить конкретный элемент списка (по тексту)
cast.remove('Chapman')

fav_movies = ['the holy grail', 'the life of Brian']
# цикл FOR
for each_movie in fav_movies:
    print(each_movie)

# цикл WHILE
i = 0
while i < len(fav_movies):
    print(fav_movies[i])
    i = i + 1

# Вложенные массивы
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
           ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle"]]]

# print (movies)
#       ['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91, ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle']]]
# print (movies[0])
#       The Holy Grail
# print (movies[1])
#       1975
# print (movies[2])
#       Terry Jones & Terry Gilliam
# print (movies[3])
#       91
# print (movies[4])
#       ['Graham Chapman', ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle']]
# print (movies[4][0])
#       Graham Chapman
# print (movies[4][1])
#       ['Michael Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idle']
# print (movies[4][1][0])
#       Michael Palin
# print (movies[4][1][1])
#       John Cleese
# print (movies[4][1][2])
#       Terry Gilliam
# print (movies[4][1][3])
#       Eric Idle

# Является ли переменна массивом (списком/листом)
names = ['Alex', 'Kate']
isinstance(names, list)
# true
num_names = len(names)
isinstance(num_names, list)
# false

# разбор вложенного массива (2 уровня)
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)

# разбор вложенного массима (3 уровня)
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)

# Посмотреть все методы Python:
dir(__builtins__)
# Чтобы получить описание конкретного (например sum), нужно ввести:
help('sum')


# Вместо разбора списка с N-количеством вложений, можно использовать функцию с использованием цикла
def function_name(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            function_name(each_item)
        else:
            print(each_item)


# Первый вариант комментариев (построчный)
""" Второй вариант комментариев (многострочный) """

import nester

cast = ['Palin', 'Cleese', 'Idle', 'Jones', 'Gilliam', 'Chapman']
nester.print_lol(cast)

print (cast)