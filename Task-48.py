array = [5, 7, 11, 13, 15, 20, 25]
array2 = []

for i in array:
    if i > 10:
        array2.append(i)

print(sum(array2) / len(array2))