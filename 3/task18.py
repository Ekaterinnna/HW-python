"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

5
1 2 3 4 5
6

-> 5
"""

import random
N = int(input('Введите N - число элементов в массиве: '))
A = []
max = 10
i = 0
for i in range(N):
    A.insert(i, random.randrange(max))
print(A)
X = int(input('Введите X: '))

dif = max
mark = A[0]
j = 0
for j in range(N):
    if abs(X - A[j]) < dif:
        dif = abs(X - A[j])
        mark = A[j]

print(mark)