# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
float_list = [1.3, 1, 3.5, 5.1, 10.02]
maxiest = float_list[0] % 1
miniest = float_list[0] % 1

for i in float_list:
    if i % 1 > maxiest:
        maxiest = i % 1 
    elif i % 1 == 0:
        continue  
    elif i % 1 < miniest:
        miniest = i % 1  
    
    
print(round(maxiest - miniest, 2))