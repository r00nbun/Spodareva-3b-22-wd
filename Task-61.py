import math

mylist = [(1, 2), (3, 4), (-1, 5), (6, -3)]

def length(element):
    return math.dist((0, 0), element)

list = sorted(mylist, key=length)
print(list)