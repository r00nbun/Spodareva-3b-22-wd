try:
    a = int(input('Ввод: '))
    b = int(input('Ввод: '))

    result = a / b
    print(result)

except ValueError:
    print('Ошибка')
except ZeroDivisionError:
    print('Ошибка')