'''Задача 1:
Напишите программу, которая запрашивает у пользователя ввод числа
и выводит на экран все числа от 1 до введенного числа включительно.'''

# Цикл for
num = int(input("Введите число: "))
for i in range(1, num + 1):
    print(i)

print()

# Цикл while
'''
num = int(input("Введите число: "))
i = 1
while i <= num:
    print(i)
    i += 1

print()
'''

'''Задача 2:
Напишите программу, которая запрашивает у пользователя ввод 2 чисел 
и выводит на экран большее из них.'''

num_one = int(input("Введите первое число: "))
num_two = int(input("Введите второе число: "))
# print(max(num_one, num_two)
if num_one > num_two:
    print('Большое число:', num_one)
elif num_two > num_one:
    print('Большое число:', num_two)
else:
    print('Числа равны')
