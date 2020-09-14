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

# Используем функцию nester.py из папки nester
import nester

cast = ['Palin', 'Cleese', 'Idle', 'Jones', 'Gilliam', 'Chapman']
nester.print_lol(cast)

print(cast)

# Генерация чисел в указанном диапазоне
for num in range(4):
    print(num)


# Создание функции с добавлением табуляции по каждому уровню вложения
def print_lol1(the_list, level):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol1(each_item, level + 1)
        else:
            for tab_stop in range(level):
                print("\t", end='')
            print(each_item)


print_lol1(movies, 0)

# Еще 1 пример
names = ['John', 'Eric', ['Cleese', 'Idle'], 'Michael', ['Palin']]
print_lol1(names, 0)


# Добавляем третий аргумент для функции, с помощью которого регулируем, нужен нам отступ или нет)
def print_lol2(the_list, indent=False, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol2(each_item, indent, level + 1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='')
            print(each_item)


print_lol2(names)  # без табуляции
print_lol2(names, True)  # с табуляцией
print_lol2(names, True, 4)  # c табуляцией + отступ

"""
import os
os.getcwd()
os.chdir('nester/HeadFirstPython/chapter3')
os.getcwd() 
"""

# В папку nester есть папка HeadFirstPython, в ней папка chapter3, в ней файл с данными sketch.txt
# Выводим на печать данные из файла
data = open('nester/HeadFirstPython/chapter3/sketch.txt')
print(data.readline(), end='')  # Первая строка
print(data.readline(), end='')  # Вторая строка и тд

data.seek(0)  # возврат к началу файла

"""for each_line in data:
    print (each_line, end='')  # Вывод на печать всего файла
data.seek(0)"""

# обработка ошибок через if (проверка на наличие двоеточия)
data = open('nester/HeadFirstPython/chapter3/sketch.txt')
for each_line in data:  # Разделение текста знаком ":"  на "до" - role и "после" - text и вывод на печать с добавлением " said " по центру
    if not each_line.find(':') == -1:  # Добавляем проверку на наличие двоетоия в строке
        (role, text) = each_line.split(':', 1)  # разделение 1 против всех. нужно для случаев, когда в строке несколько ":"
        print(role, end='')
        print(' said: ', end='')
        print(text, end='')
    else:
        print (each_line, end='')
data.close()  # Закрываем файл после завершения заботы с ним.

print ('', end='\n')  # Перенос на новую строку

# Пробуем выполнить код. Если появляется ошибка - пропускаем (либо показываем сообщение, что тут ошибка).
data = open('nester/HeadFirstPython/chapter3/sketch.txt')
for each_line in data:  # Разделение текста знаком ":"  на "до" - role и "после" - text и вывод на печать с добавлением " said " по центру
    try:
        (role, text) = each_line.split(':', 1)  # разделение 1 против всех. нужно для случаев, когда в строке несколько ":"
        print(role, end='')
        print(' said: ', end='')
        print(text, end='')
    except:
        print ('!!!!!!!!!!!!!!!SOME MISTAKES HERE!!!!!!!!!!!!!!!!', end='') # Показываем сообщение об ошибке вместо строки
        pass
data.close()  # Закрываем файл после завершения заботы с ним.



print ('', end='\n')  # Перенос на новую строку

# Проверка на наличие ":"
a = 'I tell you, theres no such thing as a flying circus.'
print(a.find(':'))
# Ответ: -1 (т.е. не содержит)
b = 'I tell you: theres no such thing as a flying circus.'
print(b.find(':'))
# Ответ: 10 (т.е. содержит)


# Проверка на наличие файла
import os
if os.path.exists('nester/HeadFirstPython/chapter3/sketch.txt'):
    data = open ('nester/HeadFirstPython/chapter3/sketch.txt')
    for each_line in data:
        if not each_line.find(':') == -1:
            (role, text) = each_line.split(':', 1)
            print (role, end='')
            print(' said: ', end='')
            print (text, end='')
    data.close()
else:
    print ('The data file is missing!')

# Проверка на выполнение скрипта (аналогично предыдущему варианту)
try:
    data = open ('nester/HeadFirstPython/chapter3/sketch.txt')
    for each_line in data:
        if not each_line.find(':') == -1:
            (role, text) = each_line.split(':', 1)
            print (role, end='')
            print(' said: ', end='')
            print (text, end='')
    data.close()
except:
    print ('The data file is missing!')

print ('', end='\n')  # Перенос на новую строку
print ('last issue:')
print ('', end='\n')

# Итого: Самый удачный вариант из всех:
"""
Вместо первоочередной обработки всех возможный вариантов мы сперва пишем сам код, 
и только потом будем обрабатывать ошибки. Если что-то пойдет не так, то мы получим сообщение об ошибке и будем знать,
что необходимо исправить в коде. 
"""
try: # первая проверка: если что-то пойдет не так с открытием файла, получим сообщение 'The data file is missing!'
    data = open('nester/HeadFirstPython/chapter3/sketch.txt')
    for each_line in data:
        try: # вторая проверка: если что-то пойдет не так с обработкой текста, получим сообщение '!!! Something goes wrong !!!!'
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except ValueError: # исключения - ошибки со значениями
            print('!!! Something goes wrong !!!!')
    data.close()
except IOError: # исключения - ошибки с  открытием файла
    print('The data file is missing!')