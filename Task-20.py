import random

my_list = [random.randint(1, 100) for i in range(10)]
print(max(my_list), min(my_list))