# Для удобства добавил функцию печати
def printArray(array):
    for j in range(len(array)):  # range(stop)/range(start, stop)/range(start, stop, step)
        for i in range(len(array[j])):
            print("{:4d}".format(array[j][i]),end='')  # ("{:2d}".format()) - Выравнивание по правому краю, ширина 4, пустое место заполняется пробельнами символами
        print()  # переход на новую строку

# Заполнение матрицы через numpy
"""
1 2 3 
4 5 6
7 8 9
"""

import numpy as np  # Добавляем поддержку массивов и матриц

a = 6  # кол-во строк
b = 6  # кол-во столбцов
c = a * b + 1
matrix = np.arange(1, c).reshape(a, b)  # Генерируем матрицу со здначениями по возрастанию от 1 до c и размером a*b
print('numpy matrix: ', end='\n')
printArray(matrix)  # нормальная матрица (без изменений)


# 1) Заполнение матрицы через цикл _________________________________
"""
1 2 3 
4 5 6
7 8 9
"""
n = 4  # строки
# m = 4  # столбцы
array = [0] * n
for i in range(n):
    array[i] = [0] * n
# создали массив: [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for i in range(0, n):
    for j in range(0, n):
        array[i][j] = i * n + j + 1
print('1 задача: ', end='\n')
printArray(array)
# __________________________________________________________________

# 2) Заполнение матрицы через цикл _________________________________
"""
1 2 3 
6 5 4
7 8 9
"""
n = 4  # строки
# m = 4  # столбцы
array = [0] * n
for i in range(n):
    array[i] = [0] * n
for i in range(0, n):  # строка
    for j in range(0, n):
        if i%2==0:
            array[i][j] = i*n+j+1
        else:
            array [i][j] = i*n+n-j
print('2 задача: ', end='\n')
printArray(array)
# __________________________________________________________________
# 3) Заполнение матрицы через цикл _________________________________
"""
1 6 7 
2 5 8
3 4 9
"""
n = 4  # строки
# m = 4  # столбцы
array = [0] * n
for i in range(n):
    array[i] = [0] * n
for i in range(0, n):  # строка
    for j in range(0, n):
        if i%2==0:
            array[j][i] = i*n+j+1
        else:
            array [j][i] = i*n+n-j
print('3 задача: ', end='\n')
printArray(array)
# __________________________________________________________________
