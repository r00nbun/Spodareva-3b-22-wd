try:
    file = open('file.txt', 'r')
    print(file.read())

except FileNotFoundError:
    print('Файл не найден')