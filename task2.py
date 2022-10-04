
# Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и последний 
# элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
nums_list = [2, 3, 4, 5, 6]
j= -1
if len(nums_list)%2 == 0:
    for i in range(int(len(nums_list)/2)):
        print(nums_list[i] * nums_list[j])
        j-= 1
else:
    for i in range(int(len(nums_list)/2 + 1)):
        print(nums_list[i] * nums_list[j])
        j-= 1