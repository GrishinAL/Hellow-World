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

# Используем функцию nester_wtf.py из папки nester


cast = ['Palin', 'Cleese', 'Idle', 'Jones', 'Gilliam', 'Chapman']
# print_lol(cast)

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
        (role, text) = each_line.split(':',
                                       1)  # разделение 1 против всех. нужно для случаев, когда в строке несколько ":"
        print(role, end='')
        print(' said: ', end='')
        print(text, end='')
    else:
        print(each_line, end='')
data.close()  # Закрываем файл после завершения заботы с ним.

print('', end='\n')  # Перенос на новую строку

# Пробуем выполнить код. Если появляется ошибка - пропускаем (либо показываем сообщение, что тут ошибка).
data = open('nester/HeadFirstPython/chapter3/sketch.txt')
for each_line in data:  # Разделение текста знаком ":"  на "до" - role и "после" - text и вывод на печать с добавлением " said " по центру
    try:
        (role, text) = each_line.split(':',
                                       1)  # разделение 1 против всех. нужно для случаев, когда в строке несколько ":"
        print(role, end='')
        print(' said: ', end='')
        print(text, end='')
    except:
        print('!!!!!!!!!!!!!!!SOME MISTAKES HERE!!!!!!!!!!!!!!!!',
              end='')  # Показываем сообщение об ошибке вместо строки
        pass
data.close()  # Закрываем файл после завершения заботы с ним.

print('', end='\n')  # Перенос на новую строку

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
    data = open('nester/HeadFirstPython/chapter3/sketch.txt')
    for each_line in data:
        if not each_line.find(':') == -1:
            (role, text) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(text, end='')
    data.close()
else:
    print('The data file is missing!')

# Проверка на выполнение скрипта (аналогично предыдущему варианту)
try:
    data = open('nester/HeadFirstPython/chapter3/sketch.txt')
    for each_line in data:
        if not each_line.find(':') == -1:
            (role, text) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(text, end='')
    data.close()
except:
    print('The data file is missing!')

# Итого: Самый удачный вариант из всех:
"""
Вместо первоочередной обработки всех возможный вариантов мы сперва пишем сам код, 
и только потом будем обрабатывать ошибки. Если что-то пойдет не так, то мы получим сообщение об ошибке и будем знать,
что необходимо исправить в коде. 
"""
try:  # первая проверка: если что-то пойдет не так с открытием файла, получим сообщение 'The data file is missing!'
    data = open('nester/HeadFirstPython/chapter3/sketch.txt')
    for each_line in data:
        try:  # вторая проверка: если что-то пойдет не так с обработкой текста, получим сообщение '!!! Something goes wrong !!!!'
            (role, text) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(text, end='')
        except ValueError:  # исключения - ошибки со значениями
            print('!!! Something goes wrong !!!!')
    data.close()
except IOError:  # исключения - ошибки с  открытием файла
    print('The data file is missing!')

# Разделяем диалог на 2 списка
man = []
other = []
try:
    data = open('nester/HeadFirstPython/chapter3/sketch.txt')
    for each_line in data:
        try:
            (role, text) = each_line.split(':', 1)
            text = text.strip()  # Удаляем лишние пробелы
            if role == 'Man':
                man.append(text)  # Добавляем элемент в конец списка
            elif role == 'Other Man':
                other.append(text)  # Добавляем элемент в конец списка
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing')
print(man)
print(other)

print('', end='\n')  # Перенос на новую строку
print('last issue:')
print('', end='\n')

# range(стоп) от 0 до стоп (не включая стоп)
# range(старт, стоп) от старт (включительно) до стоп (не включая стоп)
# range(старт, стоп, шаг) [старт стоп) шаг

# Сохранение в файл:
man = []
other = []
try:
    data = open('nester/HeadFirstPython/chapter3/sketch.txt')
    for each_line in data:
        try:
            (role, text) = each_line.split(':', 1)
            text = text.strip()  # Удаляем лишние пробелы
            if role == 'Man':
                man.append(text)  # Добавляем элемент в конец списка
            elif role == 'Other Man':
                other.append(text)  # Добавляем элемент в конец списка
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing')

try:
    man_file = open('nester/HeadFirstPython/chapter3/man_data.txt',
                    'w+')  # 'w' - данные очищаются и вносятся новые // еще есть w+ но разницу не понял
    other_file = open('nester/HeadFirstPython/chapter3/other_data.txt',
                      'w+')  # 'a' - данные не очищаются, добавляется новая строка после каждого выполнения скрипта
    # Если файла нет, то он создается.
    print(man, file=man_file)  # Вместо печати ижет сохранение в файл
    print(other, file=other_file)

    man_file.close()  # закрытие файла после использования
    other_file.close()
except IOError:
    print('File error.')
finally:  # Обеспечение правильного закрытия файлов (даже при возникновении ошибок записи)
    man_file.close()
    other_file.close()

"""
"r"   Opens a file for reading only.
"r+"  Opens a file for both reading and writing.
"rb"  Opens a file for reading only in binary format.
"rb+" Opens a file for both reading and writing in binary format.
"w"   Opens a file for writing only.
"a"   Open for writing.  The file is created if it does not exist.
"a+"  Open for reading and writing.  The file is created if it does not exist.
"""

# Учимся находить конкретную проблему в процессе записи файла
try:
    data = open('nester/HeadFirstPython/chapter3/missing.txt', 'r')
    print(data.readline(), end='')
except IOError as err:  # '... + str(err)' показывает конкретное место ошибки
    print('File error: ' + str(err))  # '... + str(err)' показывает конкретное место ошибки
finally:
    if 'data' in locals():  # Проверка на существование имени "data" в текущей области.
        # Оператор "in" проверяет вхождение в что-либо
        # Функция locals () BIF возвращает набор имен, определенных в текущей области.
        data.close()
        print('zbs')
    else:
        print('ne zbs')

    # Заменяем схему try/except/finally на try with/except (часть 1)
    # Стандартный паттерн:
    try:
        data = open('nester/HeadFirstPython/chapter3/its.txt', "w")
        print("It's...", file=data)
    except IOError as err:
        print('File error: ' + str(err))
    finally:
        if 'data' in locals():
            data.close()

    # Упрощенный вариант:
    try:
        with open('nester/HeadFirstPython/chapter3/its.txt', "w") as data:
            print("It's...", file=data)
    except IOError as err:
        print('File error: ' + str(err))

    # Заменяем схему try/except/finally на try with/except (часть 2)
    # До:
    try:
        man_file = open('nester/HeadFirstPython/chapter3/man_data.txt', 'w')
        other_file = open('nester/HeadFirstPython/chapter3/other_data.txt', 'w')

        print(man, file=man_file)
        print(other, file=other_file)
    except IOError as err:
        print('File error: ' + str(err))
    finally:
        if 'man_file' in locals():
            man_file.close()
        if 'other_file' in locals():
            other_file.close()

    # После:
    try:
        with open('nester/HeadFirstPython/chapter3/man_data.txt', 'w') as man_file:
            print(man, file=man_file)
        with open('nester/HeadFirstPython/chapter3/other_data.txt', 'w') as other_file:
            print(other, file=other_file)
    except IOError as err:
        print('File error: ' + str(err))

    # Еще после:
    try:
        with open('nester/HeadFirstPython/chapter3/man_data.txt', 'w') as man_file, open(
                'nester/HeadFirstPython/chapter3/other_data.txt', 'w') as other_file:
            print(man, file=man_file)
            print(other, file=other_file)
    except IOError as err:
        print('File error: ' + str(err))

# Учимся менять формат данных, в котором они харнятся
"""
def print_lol(the_list, indent=False, level=0, fh=sys.stdout):  # Четвертый аргумент к вашей функции print_lol (), чтобы определить место для записи ваших данных, не забудьте указать своему аргументу значение по умолчанию sys.stdout, чтобы он продолжал писать на экран, если объект файла не указывается при вызове функции.
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=fh)
            print(each_item, file=fh)
"""
import sys
from nester import nester
# import nester
# from new_nester import my_nester



# from .nester import nester

try:
    with open('nester/HeadFirstPython/chapter3/man_data.txt', 'w') as man_file, open(
            'nester/HeadFirstPython/chapter3/other_data.txt', 'w') as other_file:
        # nester.print_lol4(man) тест
        # nester.print_lol4(other) тест
        nester.print_lol5(man, fh=man_file)
        nester.print_lol5(other, fh=other_file)
except IOError as err:
    print('File error: ' + str(err))


# Моудль pickle (хранение и вывод данных)

# pickle.dump() - записываеи объект в файл (поток байтов)
# pickle.load() - загружает объект (поток байтов) из файла

import pickle

with open('nester/HeadFirstPython/chapter3/mydata.pickle', 'wb') as mysavedata:  # внимание на wb write bite
    pickle.dump([1, 2, 'three'], mysavedata)
with open('nester/HeadFirstPython/chapter3/mydata.pickle', 'rb') as myrestoredata:
    a_list = pickle.load(myrestoredata)
print(a_list)

try:
    with open('nester/HeadFirstPython/chapter3/man_data.txt', 'wb') as man_file, open('nester/HeadFirstPython/chapter3/other_data.txt', 'wb') as other_file:
        pickle.dump(man, man_file)
        pickle.dump(other, other_file)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))

# с огурчиком разобрался

# тут крч загрузил hfpy_ch5_data. в нем 4 txt файлика: james, julie, mikey, sarah


with open('nester/HeadFirstPython/hfpy_ch5_data/james.txt') as james_file:
    data = james_file.readline()  # считываем 1 строку
james = data.strip().split(',')  # убираем лишние пробелы и заделяем на отдельные элементы запятой и создавая список с соответствующими элементами
with open('nester/HeadFirstPython/hfpy_ch5_data/julie.txt') as julie_file:
    data = julie_file.readline()
julie = data.strip().split(',')
with open('nester/HeadFirstPython/hfpy_ch5_data/mikey.txt') as mikey_file:
    data = mikey_file.readline()
mikey = data.strip().split(',')
with open('nester/HeadFirstPython/hfpy_ch5_data/sarah.txt') as sarah_file:
    data = sarah_file.readline()
sarah = data.strip().split(',')

print(james)
print(julie)
print(mikey)
print(sarah)

# ____________
# Сортировки
# .sort() сортирует существующий список
data = [6,3,1,2,4,5]
print(data)
data.sort()  # тут
print('data with .sort(): ', data)

# sorted() сортирует копию списка
data = [6,3,1,2,4,5]
print(data)
data2 = sorted(data)  # тут
print('sorted() data: ', data2)
print(data)
# ____________


print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_time in james:
    clean_james.append(sanitize(each_time))
for each_time in julie:
    clean_julie.append(sanitize(each_time))
for each_time in mikey:
    clean_mikey.append(sanitize(each_time))
for each_time in sarah:
    clean_sarah.append(sanitize(each_time))
print ('sorted time:')
print(sorted(clean_james, reverse=False))  # reverse=True - порядок убывания, False - возрастание (по умолчанию)
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))