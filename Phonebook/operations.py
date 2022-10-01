

global t
global c

t='contacts.txt'
c='contacts.csv'

def print_phone_book(file):
    """
    Показывает всю телефонную книгу
    """
    with open(file, encoding='utf-8') as file  :
        for line in file:
            print(line,end='')
    file.close()


def search_contact(contact):
    """
    Ищет контакт по запросу
    """
    with open(t,'r', encoding='utf-8') as f:
        for line in f: 
            if contact in line:
                print(line)
                contact=line
        return contact

def replace_phone_contact(contact,new_contact):
    """
    Редактирует контакт
    """
    f = open(t, 'r',encoding = 'utf-8')
    lines = f.readlines()
    f.close()
    f = open(t, 'w',encoding = 'utf-8')
    for line in lines: 
        if line!=contact:
            f.write(line)
        elif line==contact:
            f.write(f'{new_contact}\n')
    f.close()           

def save_phone_number(book):
    """
    Функция записывает новый контакт
    """
    with open(t, 'a', encoding='utf-8') as data:
        data.write(f"\n{book}")

def export(c,t):
    '''
    Записывает все данные из файла c в файл t
    '''
    with open( c , 'a', encoding = 'utf-8') as file: # файл назначения
        for line in open(t, encoding = 'utf-8'):
            file.write(line)

def del_phone_number(contact):
    """
    Удаляет контакт
    """
    f = open(t, 'r',encoding = 'utf-8')
    lines = f.readlines()
    f.close()
    f = open(t, 'w',encoding = 'utf-8')
    for line in lines: 
        if line!=contact:
            f.write(line)
    f.close()
    



# book=str(input('Введите: '))
# save_phone_number(book)

