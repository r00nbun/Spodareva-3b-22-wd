import random

my_list = [random.randint(1, 10) for i in range(10)]
if my_list.count(int(input('Ввод: '))) == True:
    print('Число найдено в массиве')
else:
    print('Число не найдено в массиве')