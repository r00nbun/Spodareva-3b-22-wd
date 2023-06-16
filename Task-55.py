try:
    a = input('Ввод: ').split()
    mylist = [int(x) for x in a]
    mylist.sort()
    print(mylist[0])

except ValueError:
    print('Ошибка')
