# from array import *

a = [3, 2, 6, 2, 8, 1, 0, 1, 6, 0]
b = [1, 0, 1, 0, 0]


for i in range(0, 6):
    if a[i] == b[0]:
        for j in range(1, 5):
            if a[i+1] == b[j]:
                print('true')
                i=i+1
            else:
                print('false')
    else:
        print('false')
