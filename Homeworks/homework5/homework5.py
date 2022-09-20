# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

line ='абвгдейка - это передача'
print(line)
fragment = 'абв'
def del_fragment():
    words = line.split(' ')
    new_words = []
    for word in words:
        if fragment not in word:
            new_words.append(word)
    new_words
    print(' '.join(new_words))
del_fragment()

# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
count=10
max_num=3

def input_number(max_num,count,plaer):
    '''Ввод числа, удовлетворяющего условию задачи'''
    flag = False
    while not flag:
        try:
            number = int(input(f'Игрок {plaer}, возьмите конфеты от 1 до {max_num} штук:')) 
            flag=True
            if (0>=number or number>max_num or number>count):
                flag=False
                print('Вы ввели неверное возможное количество конфет за ход!')
        except ValueError:
                print('Это не число!')
    return number

def player_vs_player(count):
    """ Игрок против игрока"""
    draw=random.randint(1,2)
    if draw ==1:
        print('По результату жеребьевки ходит Игрок 1')
        while count>0:
            if count>0: 
                player=1
                player_num=input_number(max_num,count,player)
                count-=player_num
                print(f'осталось {count} конфет')
            if count>0:        
                player=2
                player_num=input_number(max_num,count,player)
                count-=player_num
                print(f'осталось {count} конфет')
        print(f'Игрок {player}, Вы проиграли')
    if draw ==2:
        print('По результату жеребьевки ходит Игрок 2')
        while count>0:
            if count>0:        
                player=2
                player_num=input_number(max_num,count,player)
                count-=player_num
                print(f'осталось {count} конфет')
            if count>0: 
                player=1
                player_num=input_number(max_num,count,player)
                count-=player_num
                print(f'осталось {count} конфет')
        print(f'Игрок {player}, Вы проиграли')

def player_vs_random_bot(count):
    """Игрок против "случайного" бота """  
    draw=random.randint(1,2)
    if draw ==1:
        print('По результату жеребьевки ходит Игрок 1')
        while count>0:
            if count>0: 
                player=1
                player_num=input_number(max_num,count,player)
                count-=player_num
                print(f'осталось {count} конфет')
            if count>0:
                player='"случайный" бот'
                player_num=random.randint(1,max_num)        
                while (player_num>count):
                    player_num=random.randint(1,max_num) 
                print(f'Бот взял {player_num} конфет')
                count-=player_num
                print(f'осталось {count} конфет')
        print(f'Игрок {player} проиграл')
    if draw ==2:
        print('По результату жеребьевки ходит "случайный" бот')
        while count>0:
            if count>0:
                player='"случайный" бот'
                player_num=random.randint(1,max_num)        
                while (player_num>count):
                    player_num=random.randint(1,max_num) 
                print(f'Бот взял {player_num} конфет')
                count-=player_num
                print(f'осталось {count} конфет')
            if count>0: 
                player=1
                player_num=input_number(max_num,count,player)
                count-=player_num
                print(f'осталось {count} конфет')
        print(f'Игрок {player} проиграл')

def player_vs_smart_bot(count):
    """Игрок против "умного" бота """
    draw=random.randint(1,2)
    if draw ==1:
        print('По результату жеребьевки ходит Игрок 1')
        while count>0:
            if count>0: 
                player=1
                player_num=input_number(max_num,count,player)
                count-=player_num
                print(f'осталось {count} конфет')
            if count>0:
                player='"умный" бот'
                if ((count-1)%(1+max_num))!=0:
                    player_num=((count-1)%(1+max_num))
                elif count%max_num==0: 
                    player_num=max_num
                if count==1:
                    player_num=1        
                print(f'Бот взял {player_num} конфет')
                count-=player_num
                print(f'осталось {count} конфет')
        print(f'Игрок {player} проиграл')
    if draw ==2:
        print('По результату жеребьевки ходит "умный" бот')
        while count>0:
            if count>0:
                player='"умный" бот'
                if ((count-1)%(1+max_num))!=0:
                    player_num=((count-1)%(1+max_num))
                elif count%max_num==0: 
                    player_num=max_num
                if count==1:
                    player_num=1        
                print(f'Бот взял {player_num} конфет')
                count-=player_num
                print(f'осталось {count} конфет')
            if count>0: 
                player=1
                player_num=input_number(max_num,count,player)
                count-=player_num
                print(f'осталось {count} конфет')
        print(f'Игрок {player} проиграл')

def mode_of_game():
    """Выбор режима игры"""
    mode=int(input('Введите режим игры от 1 до 3, где:\n 1 - это игра против человека\n 2 - это игра против "случайного" бота \n 3 - это игра против "умного" бота\n '))
    if mode==1:
        player_vs_player(count)
    if mode==2:
        player_vs_random_bot(count)
    if mode==3:
        player_vs_smart_bot(count)

mode_of_game()
   
# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже,
# то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, 
# в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

# Дополнительно(по желанию):
# 1 - Создайте программу для игры в ""Крестики-нолики"".
# 2 - Создать программу, считывающую два полинома из двух файлов и записывающая в третий файл их сумму.

list1=['python', 'c#', 'c++', 'java','javascript','php','css']
list2=[i for i in range(1,len(list1)+1)]
print(list1)
print(list2)
num_lang=list(zip(list2,list(map(lambda f: f.upper(),list1))))
print(num_lang)
def filter(list):
    end_list=[]
    sum_ord=0
    for n,l in list:
        for i in l:
            sum_ord+=ord(i)
        if sum_ord%n==0:
            end_list.append((sum_ord,l))
    print(end_list)
filter(num_lang)