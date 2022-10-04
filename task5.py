# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
# Пример:для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
n = int(input('Введите число: '))  
def positive_fib(n):
    if n == 0:
        return 0
    elif n in [1, 2]:
        return 1
    else:
        return positive_fib(n-1)+ positive_fib(n-2)    
def negative_fib(n):
    
    if n == 1:
        return 1
    elif n == 2:
        return -1    
    else:
        return negative_fib(n-2) - negative_fib(n-1)   
fib_list =[]
for i in range(2, n +1):
    fib_list.insert(0, negative_fib(i))
for e in range(0, n +1):
    fib_list.append(positive_fib(e))
print(fib_list)