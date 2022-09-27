import operations as calcul
import user_interface as ui
import log



def button_click():
    '''
    Функция запрашивает данные, решает и выводит    
    '''
    global name
    while True:    
        name = ui.choice_calc('')
        
        if name == 1:
            first_r = ui.rational_number(1)
            sign = ui.operation(' ')
            second_r = ui.rational_number(2)
            second_mn = 0
            calcul.init_ratio(first_r, second_r)
        elif name == 2:
            first_r, first_mn = ui.complex_number(1)
            sign = ui.operation(' ')
            second_r, second_mn = ui.complex_number(2)
            calcul.init_compl(first_r, first_mn, second_r, second_mn)
        elif name==3:
            break
        if sign == '+':
            result = calcul.sum()
        if sign == '-':
            result = calcul.sub()
        if sign == '*':
            result = calcul.mult()
        if sign == '/':
            result = calcul.div()
        if name == 1:
            result = round(result, 5)
        if result == False:
            result = 'Деление на 0 невозможно!'
            print(result)

        data_log = str(calcul.x) + ' ' + sign + ' ' + str(calcul.y)
        ui.output_result(data_log, result)
        log.logger(data_log, result)
        