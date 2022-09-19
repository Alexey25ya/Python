# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

# line ='абвгдейка - это передача'
# print(line)
# fragment = 'абв'
# def del_fragment():
#     words = line.split(' ')
#     new_words = []
#     for word in words:
#         if fragment not in word:
#             new_words.append(word)
#     new_words
#     print(' '.join(new_words))
# del_fragment()

# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""


count=10
max_num=3

def input_number(max_num,count,plaer):
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

def player_vs_player():
    while count>0:
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

import random
def player_vs_random_bot():
    while count>0:
        player=1
        player_num=input_number(max_num,count,player)
        count-=player_num
        print(f'осталось {count} конфет')
        if count>0:
            player='бот'
            player_num=random.randint(1,max_num)        
            while (player_num>count):
                player_num=random.randint(1,max_num) 
            print(f'Бот взял {player_num} конфет')
            count-=player_num
            print(f'осталось {count} конфет')
    print(f'Игрок {player}, Вы проиграли')

def player_vs_smart_bot():
    while count>0:
        player=1
        player_num=input_number(max_num,count,player)
        count-=player_num
        print(f'осталось {count} конфет')
        if count>0:
            player='бот'
            if ((count-1)%(1+max_num))!=0:
                player_num=((count-1)%(1+max_num))
                print('b',player_num,count)
            elif count%max_num==0: 
                player_num=max_num 
                print('c',player_num,count)
            if count==1:
                player_num=1        
            print(f'Бот взял {player_num} конфет')
            count-=player_num
            print(f'осталось {count} конфет')
    print(f'Игрок {player}, Вы проиграли')



#3. добавить бота рандом от 1 до 28
#4. добавить бота,который стремится выиграть
#5. добавить выбор между вариациями человек,бот рандом, "умный" бот




#

# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

# Дополнительно(по желанию):
# 1 - Создайте программу для игры в ""Крестики-нолики"".
# 2 - Создать программу, считывающую два полинома из двух файлов и записывающая в третий файл их сумму.