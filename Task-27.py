import random

my_list = [random.randint(1, 10) for i in range(10)]
list = []
for i in my_list:
    if i%2==0:
        list.append(i)
print(list)
