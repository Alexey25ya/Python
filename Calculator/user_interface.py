import check as ch
from colorama import Fore,Back

def rational_number(number:str) -> float:
    '''
    Ввод рационального числа
    '''
    input_data = Fore.BLUE + f'Введите {number} рациональное число: '
    return ch.check_float_number(input_data)

def complex_number(number:str) -> complex:
    '''
    Ввод комплексного числа
    '''
    input_d = Fore.GREEN + f'Введите действительную часть {number} числа: ' +Fore.WHITE
    input_mn = Fore.GREEN + f'Введите мнимую часть {number} числа: ' +Fore.WHITE
    return ch.check_float_number(input_d), ch.check_float_number(input_mn)

def operation(oper:str) -> str:
    '''
    Ввод операции
    '''
    input_sign = Fore.YELLOW + f'Введите знак операции: (+, -, *, /):{oper}' +Fore.WHITE
    return ch.check_symbol(input_sign)

def choice_calc(number:str) -> int:
    '''
    Выбор калькулятора комплексных или рациональных чисел
    '''
    print(Fore.MAGENTA+'Для выбора калькулятора рациональных чисел нажмите 1, для комплексных нажмите 2, для выхода из калькулятора нажмите 3: ' +Fore.WHITE)
    return ch.check_calc(number)

def output_result(data, res):
    '''
    Вывод результата
    '''
    print(Fore.YELLOW + f"Для этого примера: {data} ответ будет: {res}" +Fore.WHITE)