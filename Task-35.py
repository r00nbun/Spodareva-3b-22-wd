fib1 = fib2 = 1
print(fib1, fib2, end=' ')

n = int(input('Количество чисел ряда Фибоначчи: '))
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')