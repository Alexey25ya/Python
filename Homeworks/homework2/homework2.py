# # 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
# # Учтите, что числа могут быть отрицательными
# # Пример:
# # 67.82 -> 23
# # 0.56 -> 11

print('Задание 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.')
def real_number():
    while True:
        try:
            num=float(input('Введите вещественное число: '))
            return num
        except(ValueError):
            print('Вы ввели не число')

def sumNumbers(num):
    if num<0:
        num = -1*num
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

print(sumNumbers(real_number()))

# # 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений 
# # (набор - это список) чисел от 1 до N.
# # Не используйте функцию math.factorial.
# # Пример:
# # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('Задание 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.')
def integer_number():
    while True:
        try:
            numb=int(input('Введите целое число: '))
            return numb
        except(ValueError):
            print('Вы ввели не целое число')

def factorial_list(num):
    mult=1
    list=[]
    for i in range(num):
        mult=(i+1)*mult
        list.append(mult)
    print(list)
factorial_list(integer_number())

# # 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# # А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# # Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# # Это происходит до тех пор, пока не будет найден палиндром.
# # Напишите такую программу, которая найдет палиндром введенного пользователем числа.

print('Задание 3. Напишите такую программу, которая найдет палиндром введенного пользователем числа.')
n1 = integer_number()
n_list = list(str(n1))
n_list.reverse()
n2 = "".join(n_list)
n2=int(n2)
n1=int(n1)
while n1!=n2:
    n1=n1+n2
    n_list = list(str(n1))
    n_list.reverse()
    n2 = int("".join(n_list))
print(f'Палиндром равен:',n1)

# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) 
# - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

print('Задание4 - Реализуйте выдачу случайного числа')
import time

def rand(min,max):
    random_num=(time.time_ns()/100)%100000
    while min>random_num or random_num>max:
        if  min>random_num:
            random_num*=1.1
        else :
            random_num*=0.1          
    print(f'Случайное число в заданном диапазоне равно: ',int(random_num))
min=int(input('Введите min: '))
max=int(input('Введите max: '))
rand(min,max)