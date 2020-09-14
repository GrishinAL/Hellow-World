# В рамках задачи на ст.79 создали отдельный файл, чтобы найти ошибку

data = open('sketch.txt')

for each_line in data:  # Разделение текста знаком ":"  на "до" - role и "после" - text и вывод на печать с добавлением " said " по центру
    (role, text) = each_line.split(':')
    print (role, end='')
    print(' said: ', end='')
    print (text, end='')

data.close()  # Закрываем файл после завершения заботы с ним.