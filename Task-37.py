import random

my_list = [random.randint(1, 100) for i in range(10)]

my_list.sort()
print(f'Два наименьших значения - {my_list[0]} и {my_list[1]}')