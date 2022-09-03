# 1-Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет


def weekday():
    day=int(input('Введите номер дня недели: '))
    if 1<=day<=5:
        print('нет')
    elif 6<=day<=7:
        print('да')
    else:
        print('Такого дня недели не существует!')    
weekday()
 
# 2-Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# Предикату можно заменить на понятие "бит".Должна получиться таблица истинности.

def truth_table():
 print('x    y    z    result')
 for x in (True,False):
    for y in (True,False):
        for z in (True,False):
            if not(x or y or z)== (not x and not y and not z):
                print(x,y,z,True)
            else:
                print(x,y,z,False)
truth_table()

# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def input_number(inputText):
    a = False
    while not a:
        try:
            number = float(input(f'{inputText}')) 
            a = True
            if number == 0:
                    a = False
                    print("Координата не должно быть равна 0 ")
        except ValueError:
                print('Это не число!')
    return number

def find_quater():
    if x>0 and y>0:
        print('Первая четверть')
    elif x<0 and y>0:
        print('Вторая четверть')
    elif x<0 and y<0:
        print('Третья четверть')
    else:
        print('Четвертая четверть')


x=input_number('Введите x: ')
y=input_number('Введите y: ')
find_quater()

# 4- Напишите программу, которая по заданному номеру четверти,∈ꚙ
# показывает диапазон возможных координат точек в этой четверти (x и y).

def input_num(inputText):
    a = False
    while not a:
        try:
            num = int(input(f'{inputText}')) 
            a = True
            if num>4 or num<1:
                a = False
                print('Введите целое число от 1 до 4!')
        except ValueError:
                print('Это не целое число!')
    return num

def range_coord():
    if numQuater==1:
        print('Возмщжные координаты 1 четверти: X ∈(0; ꚙ ), Y∈(0; ꚙ )')
    elif numQuater==2:
        print('Возмщжные координаты 2 четверти: X ∈(-ꚙ ;0), Y∈(0; ꚙ )')
    elif numQuater==3:
        print('Возмщжные координаты 3 четверти: X ∈(-ꚙ ;0), Y∈(0;-ꚙ )')
    else:
        print('Возмщжные координаты 4 четверти: X ∈(0; ꚙ ), Y∈(-ꚙ ;0)')
    
        

numQuater=input_num('Введите номер четверти от 1 до 4: ')
range_coord()

# 5-Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


x1=int(input('Введите координату x1 первой точки : '))
y1=int(input('Введите координату y1 первой точки : '))
x2=int(input('Введите координату x2 второй точки : '))
y2=int(input('Введите координату y2 второй точки : '))
print(f'Расстояние между точками равно: {round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (0.5),2)}')