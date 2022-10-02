from colorama import *

def check_numbers(number:str)->str:
    '''Проверка на цифры (не более 12 цифр, не допускает ввода пустой строки)'''
    while True:
        try:
            n = input(number)
            if int(n)<100000000000:
                return n
            else:
                print(Fore.RED + 'Вы ввели количество цифр больше возможного(12)! '+ Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + 'Неверно! Это не номер телефона! Вводите только цифры без пробелов!' + Style.RESET_ALL)

def check_alpha(name:str)->str:
    '''Проверка на буквы (не допускает ввода пустой строки)'''
    while True:
        try:
            a = input(name)
            if (a.isalpha() and 0<len(a)<20):
                return a
            else:
                print(Fore.RED + 'Вы ввели символы отличные от букв или большое количество символов '+ Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + 'Неверно!'+ Style.RESET_ALL)


def record_length(length:str)->str:
    '''Проверка длины вводимой строки и тут же проверка на пустую строку'''
    while True:
        try:
            l = input(length)
            if len(l)==0:
                print(Fore.RED + 'Вы ничего не ввели!'+ Style.RESET_ALL)
            elif len(l)<20:
                return l
            else:
                print(Fore.RED + 'Вы ввели слишком много символов '+ Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + 'Неверно! Повторите ввод!'+ Style.RESET_ALL)

def check_phone_menu(num:str,m)->int:
 
    while True:
        try:
            n = int(input(num))
            if 0<int(n)<m:
                return n
            else:
                print(Fore.RED + f'Неверно! Введите число от 1 до {m-1} в соответствии с пунктами меню!'+ Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + f'Неверно!Введите число от 1 до {m-1} в соответствии с пунктами меню!' + Style.RESET_ALL)

#check_phone_menu('',6)
