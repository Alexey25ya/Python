# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение
# Формат: Объясняет преподаватель

# **Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования лямбд, filter, map, zip, enumerate, list comprehension, reduce**

# 1 - Определить, присутствует ли в заданном списке строк, некоторое число

input_list=["qwe", "asd", "zxc", "2qwe", "12ertqwe",'']
num=2
output_list=[x for x in input_list for x in x if x == str(num)]
print(output_list)
result=lambda output_list:'Такое число есть в списке' if output_list!=[] else 'Такого числа нет'
print(result(output_list))

# 2 - Найти сумму чисел списка стоящих на нечетной позиции
list_num=[12,15,35,1,8,11]
out_list=[list_num[i] for i in range(len(list_num)) if i%2!=0]
print(sum(out_list))

# 3 - Найти расстояние между двумя точками пространства(числа вводятся через пробел)
list1=[int(i) for i in input('Введите координаты первой точки (x1,y1) через пробел: ').split(' ')]
list2=[int(i) for i in input('Введите координаты второй точки (x2,y2) через пробел: ').split(' ')]
print(f'Расстояние между введенными точками равно: {((list2[0]-list1[0])**2+(list2[1]-list1[1])**2)**(0.5)}')

# 4 - Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

input_list=["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
elem="йцу"
output=[i for i in range(len(input_list)) if input_list[i]==elem]
result=lambda output: f'позиция второго вхождения {output[1]}' if len(output)>1 else 'второго вхождения нет'
print(result(output))

# 5 - Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
input_list=[1,2,3,4,5,6,7]
output_list=[input_list[i]* input_list[-1-i] for i in range(len(input_list)//2 + len(input_list)%2)]
print(output_list)

# 6 - Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
n=5
res=[(-3)**i for i in range(n)]
print(res)