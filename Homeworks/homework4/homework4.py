# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]
n=int(input('Введите N: '))

def simple_num_list(num):
    '''программa, которая составит список простых множителей числа N.'''
    simple_list = []
    for i in range(2, num):
        while num % i == 0:
            num = num/i        
            simple_list.append(i)
            break
    print(simple_list)
simple_num_list(n)


# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#  Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]
list_num=[1,1,1,1,2,2,2,3,3,3,4,1,2,3,4]
list_unique=[]
for i in list_num:
    if i in list_unique:
        continue
    list_unique.append(i)
       
print(list_unique)


# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов,
#  которые имеют средний балл более «4».
# Пример:
# Волков Андрей 5
# Наталья Тарасова 5
# Фредди Меркури 3
# Денис Байцуров 4

# Программа выдаст:
# ВОЛКОВ АНДРЕЙ 5
# НАТАЛЬЯ ТАРАСОВА 5
# Фредди Меркури 3
# Денис Байцуров 4

def write(path,input_s):
    '''Ввод данных в файл'''
    data = open(path, 'w')
    data.write(input_s) 
    data.close()
def read(path):
    '''Чтение данных из файла'''
    data = open(path, 'r')
    output_s=data.readline()
    data.close()
    return output_s 


def  replace():
    with open('f3_1','r') as f1,\
        open('f3_2','w') as f2:
        for line in f1:
            list_line=line.split()
            if float(list_line[-1])>4:
                f2.write(line.upper())
            else: f2.write(line)
write('f3_1', 'Volkov Andrey 5\nNataliia Tarasova 5\nFreddy Merkury 3\nDenis Baycurov 4')
replace()

    
# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо,
#  "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, 
# считывает текст и дешифровывает его.

input_text=input('Введите текст для шифрования: ')
def caesar_encoder(st):
    key=int(input('Введите ключ для шифрования: '))
    list=[]
    for i in range(len(st)):        
        i=chr(ord(st[i])+key)          
        list.append(i)
    write('f4', (''.join(list)))        
caesar_encoder(input_text)
print(read('f4'))
def caesar_decoder(st):
    key=int(input('Введите ключ для дешифрования: '))
    list=[]
    for i in range(len(st)):
        i=chr(ord(st[i])-key)          
        list.append(i)
    return''.join(list)        
print(caesar_decoder(read('f4')))

# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

def encode(s):
    encoding = ''
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + s[i]
        i = i + 1
    return encoding

def decode(s):
    decoding=''
    count=''
    for i in range(len(s)):
        if s[i].isdigit():
            count+=s[i]
        else:
            decoding+=s[i]*int(count)
            count=''
    return decoding

input_s ='AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool'
write('file.txt',input_s)
print(read('file.txt'))
print(encode(read('file.txt')))
write('file1.txt',encode(read('file.txt')))
print(decode(read('file1.txt')))









