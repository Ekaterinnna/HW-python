"""
Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
"""

A = int(input('Введите A: '))
B = int(input('Введите B: '))

def pawNumber(b_number, p_number):
    if p_number == 1:
        return b_number
    else:
        return b_number * pawNumber(b_number, p_number-1)

print(pawNumber(A, B))