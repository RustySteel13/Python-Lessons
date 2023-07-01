# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def power(num1, num2):
    if num2 == 0:
        return 1

    return num1 * power(num1, num2 - 1)


num = power(int(input('number: ')), int(input('degree: ')))
print(f'number is {num}')