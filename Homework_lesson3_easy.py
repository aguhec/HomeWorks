# Задание - 1

# print('Привет Сенсей! мы продолжаем нашу магию!')
#
#
# def person(name, age, city):
#     result = '{}, {} год(а), Вы проживаете в городе {}\nКак вам такая магия?'.format(name, age, city)
#     return result
#
# print('Я задам вам несколько вопросов, а потом расскажу о вас занимательный факт!')
# name = input('Введите имя: ')
# age = input('Введите возраст: ')
# city = input('Введите город проживания: ')
#
# result = person(name, age, city)
# print(result)

# Задание - 2

# def max_count(a, b, c):
#     num_list = [a, b, c]
#     result = max(num_list)
#     return result
# print('Продолжаем магию!')
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# c = int(input('Введите третье число: '))
#
# print('Максимальное число которое вы ввели: ', (max_count(a,b,c)))

# Задание - 3



# def max_string(* arg):
#     max_len = max(arg, key=len)
#     return max_len
# print('Магический шар может пресказать будущее, а может выбрать самое длинное строчку!')
# arg1 = (input('Введите первую строку: '))
# arg2 = (input('Введите вторую строку: '))
# arg3 = (input('Введите третью строку: '))
# result = max_string(arg1, arg2, arg3)
# print('Вы не поверите, но самая длинная строка будет: {}'.format(result))