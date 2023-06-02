import os

check = os.path.isfile('text.txt')
if check:
    print('Файл существует')
else:
    print('Файл не существует')