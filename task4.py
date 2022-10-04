# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
num_type0 = int(input('Введите число: '))
convert_helper = ''
while num_type0 != 0:
    convert_helper = str(num_type0 % 2) + convert_helper
    num_type0 =  num_type0//2
print(convert_helper)    