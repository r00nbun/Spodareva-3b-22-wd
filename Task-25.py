number = int(input('Введите число: '))
count = 0

for i in range(2, number//2+1):
    if count%i == 0:
        count += 1
if count<=0:
    print('Введённое число простое')
else:
    print('Введённое число составное')