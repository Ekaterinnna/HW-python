"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18

6 12
"""

n = int(input('Введите n - число элементов в первом массиве: '))
m = int(input('Введите m - число элементов во втором массиве: '))

print(f'Введите {n} чисел/а через пробел:', end = ' ')
N = set(map(int, input().split()))

print(f'Введите {m} чисел/а через пробел:', end = ' ')
M = set(map(int, input().split()))

res = N.intersection(M)
print(*res)
