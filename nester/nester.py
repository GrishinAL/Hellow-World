# Вместо разбора списка с N-количеством вложений, можно использовать функцию с использованием цикла
import sys
"""
def print_lol (the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)
"""
# Сохранение в файл вложенных списков с табуляцией
def print_lol5(the_list, indent=False, level=0, fh=sys.stdout):  # Четвертый аргумент к вашей функции print_lol (), чтобы определить место для записи ваших данных, не забудьте указать своему аргументу значение по умолчанию sys.stdout, чтобы он продолжал писать на экран, если объект файла не указывается при вызове функции.
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol5(each_item, indent, level+1, fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=fh)
            print(each_item, file=fh)

# Просто печать вложенных списков с табуляцией
def print_lol4(the_list, indent=False, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol4(each_item, indent, level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='')
            print(each_item)
