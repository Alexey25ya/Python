from datetime import datetime as dt

def log(data, result):
    '''
    Записывает время, выражение и результат
    '''
    time = dt.now().strftime('%d.%m.%Y - %H:%M')
    with open('log.txt', 'a', encoding = 'UTF-8') as file:
        file.write(f'{time}: \t{data}: \t {result}\n') 