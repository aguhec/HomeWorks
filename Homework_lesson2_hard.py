# Задание-1
equation = 'y = -12x - 11111140.2121'
x = 2.5

list_graphic = equation.split()
print(list_graphic)
k = float(list_graphic[2][:-1])
b = float(list_graphic[4])
# Ниже проведена проверка, на знак b
if list_graphic[3] == '-':
    b = 0 - b
else:
    b = 0 + b
y = k * x + b
print(y)

# Задание-2:

date = '12.12.0002'
date_list = (date.split('.'))
while len(date_list[0]) != 2 or len(date_list[1]) != 2 or len(date_list[2]) != 4:  # Проверка на длинну
    print('Формат даты не верный!')
    date = input('Введите дату в формате dd.mm.yyyy: ')
date_list[2] = int(date_list[2])
while date_list[2] < 0 or date_list[2] > 9999:  # Проверка года на диапазон. Почему он мне выделяет цифры?
    print('Формат даты не верный!')
    date = input('Введите дату в формате dd.mm.yyyy: ')

dict_month = {  # Вводим словарь, для понимания количества дней в месяце
    '01': '31',
    '02': '28',
    '03': '31',
    '04': '30',
    '05': '31',
    '06': '30',
    '07': '31',
    '08': '31',
    '09': '30',
    '10': '31',
    '11': '30',
    '12': '31', }

while int(date_list[1]) < 0 or int(date_list[1]) > 12:  # Проверка что месяц в диапазоне от 0 до 12
    print('Формат даты не верный!')
    date = input('Введите дату в формате dd.mm.yyyy: ')

while int(date_list[0]) < 0 or int(date_list[0]) > int(dict_month[date_list[1]]):  # Проверяем правильное ли ко-во дней
    print('Формат даты не верный!')
    date = input('Введите дату в формате dd.mm.yyyy: ')

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)

room = 50000
claster = 0
max_in_claster = 0
max_floor_claster = 0
while room > max_in_claster:
    claster += 1
    max_in_claster = (claster ** 2) + max_in_claster
    max_floor_claster += claster
count = 0
step = 0
floor_answer = max_floor_claster
max_room_in_claster = max_in_claster

room_in_claster = claster ** 2
if room == max_in_claster:
    print('Этаж:', floor_answer, '\nКомната:', claster, 'по счету слева')
else:
    while room != max_in_claster:
        max_in_claster -= 1
        count += 1
        if count % claster == 0:
            floor_answer -= 1
            step += 1

    max_room_in_floor = max_room_in_claster - step * claster
    position = claster
    if room == max_room_in_floor:
        print('Этаж:', floor_answer, '\nКомната:', claster, 'по счету слева')
    else:
        while room < max_room_in_floor:
            max_room_in_floor -= 1
            position -= 1
        print('Этаж:', floor_answer, '\nКомната:', position, 'по счету слева')
