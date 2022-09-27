from colorama import Fore

def check_int_number(number: str) -> int:
    '''
    Поверка целого числа
    '''
    while True:
        try:
            return int(input(number))
        except ValueError:
            print(Fore.RED+f'Неверно! Должно быть целое число!')

def check_float_number(number: str) -> float:
    '''
    Поверка дробного числа
    '''
    while True:
        try:
            return float(input(number))
        except ValueError:
            print(Fore.RED+f'Неверно! Должно быть дробное число!')


def check_symbol(symbol: str) -> str:
    '''
    Поверка знака действия
    '''
    while True:
        try:
            sym = input(symbol)
            if sym == '+' or sym =='-' or sym =='*' or sym =='/':
                return sym
            else:
                print(Fore.RED+f'Неверно! Должен быть знак действия ("+", "-", "*", "/")!')
        except ValueError:
            print(Fore.RED+f'Неверно! Должен быть знак действия ("+", "-", "*", "/")!')


def check_calc(digit: str) -> int:
    '''
    Поверка выбора калькулятора
    '''
    while True:
        try:
            calc_choice = int(input(digit))
            if calc_choice == 1 or calc_choice == 2 or calc_choice==3:
                return calc_choice
            else:
                print(Fore.RED+f'Неверно! Для выбора калькулятора рациональных чисел нажмите 1, для комплексных 2,для выхода 3')
        except ValueError:
            print(Fore.RED+f'Неверно! Для выбора калькулятора рациональных чисел нажмите 1, для комплексных 2,для выхода 3')