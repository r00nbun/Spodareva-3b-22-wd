a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
command = str(input('Введите операцию (+, -, /, *): '))

if command == '+':
    print(a + b)
elif command == '-':
    print(a - b)
elif command == '/':
    print(a / b)
elif command == '*':
    print(a * b)
else:
    print('Неверная операция')