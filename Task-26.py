def lcm(a, b):
    import math
    return (a * b) // math.gcd(a, b)

a = int(input('Введите число: '))
b = int(input('Введите число: '))

print('Наименьший общий множитель: ', lcm(a, b))