# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
# - Для N = 5: 1, -3, 9, -27, 81
N=int(input('Введите N: '))
for i in range(N):
    print((-3)**i)
# 2.Найти сумму элементов массива, лежащих между максимальным и минимальным по значению элементами
# 3.Найдите количество элементов массива, которые отличны от наибольшего элемента не более чем на 10%.