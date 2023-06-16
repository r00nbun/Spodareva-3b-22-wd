n = int(input('Ввод: '))

try:
    i = 1
    a = 0
    while i <= n:
        i=+1
        a=+i
    print(a)

except ValueError:
    print('Ошибка')