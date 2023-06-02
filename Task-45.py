name = str(input('Ввод: '))

try:
    file = open(name, 'r')
    print(file.read())

except FileNotFoundError:
    print('Ошибка.')
except IOError:
    print('Ошибка')