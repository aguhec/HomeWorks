import random
import math

# Задача-1:
# Я совсем запутался, как мне выбирать какой то индекс в цикле for....
n = int(input('Введите длинну списка: '))
numbers = []
for _ in range(n):
    numbers.append(random.randint(-10, 10))
new_numbers = []
for i in numbers:
    if i > 0:
        new_numbers.append(math.sqrt(i))
result = []
for i in new_numbers:
    if i % 1 == 0:
        result.append(i)

print(result)


# Задача-2:

date = input('Введите дату в формате dd.mm.yyyy')
date_list = date.split('.')

dict_day = {'01': 'первое', '02': 'второе', '03': 'третье', '04': 'четвёртое', '05': 'пятое',
'06': 'шестое', '07': 'седьмое', '08': 'восьмое', '09': 'девятое', '10': 'десятое',
'11': 'одиннадцатое', '12': 'двенадцатое', '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое',
'16': 'шестнадцатое', '17': 'семнадцатое', '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое',
'21': 'двадцать первое', '22': 'двадцать второе', '23': 'двадцать третье', '24': 'двадцать четвёртое',
'25': 'двадцать пятое', '26': 'двадцать шестое', '27': 'двадцать седьмое', '28': 'двадцать восьмое',
'29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое',
}
dict_month = {
'01': 'января',
'02': 'февраля',
'03': 'марта',
'04': 'апреля',
'05': 'мая',
'06': 'июня',
'07': 'июля',
'08': 'августа',
'09': 'сентября',
'10': 'октября',
'11': 'ноября',
'12': 'декабря',
}
for key in dict_day:
    if date_list[0] == key:
        date_list[0] = dict_day[key]

for key in dict_month:
    if date_list[1] == key:
        date_list[1] = dict_month[key]
#convert_date = date_list[0], date_list[1], date_list[2], 'года'
#Почему если я сделаю новую переменную, то ответ будет выводится кортежем?
print(date_list[0], date_list[1], date_list[2], 'года')

# Задача-3:

n = int(input('Введите длинну списка: '))
numbers = []
for _ in range(n):
    numbers.append(random.randint(-100, 100))
print(numbers)

# Задача-4:
# а) неповторяющиеся элементы исходного списка:

n = int(input('Введите длинну списка: '))
numbers = []
for _ in range(n):
    numbers.append(random.randint(0, 10))
print(numbers)
numbers1 = list(set(numbers))

# б) элементы исходного списка, которые не имеют повторений

numbers2 = []
for i in numbers:
    if numbers.count(i) == 1:
        numbers2.append(i)
print(numbers2)