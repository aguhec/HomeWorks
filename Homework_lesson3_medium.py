import os
import math

# Задание - 1

PATH = r'C:\Users\1\Desktop\GB\untitled2'
FILE_NAME = 'salary.txt'
full_path = os.path.join(PATH, FILE_NAME)
workers = ['Андрей', 'Иван', 'Петр', 'Сергей', 'Ашот', 'Валерий Иванович']
money = [10000, 20000, 30000, 40000, 2000, 500000]
salary = dict(zip(workers, money))
# print(salary)

with open(full_path, 'w', encoding='UTF-8') as file:
    for key, item in salary.items():
        if item < 500000:
            file.write('{} - {}\n'.format(key, item))
file.close()
my_new_list = []
with open(full_path, 'r', encoding='UTF-8') as file:
    for f in file.readlines():
        my_new_list.append(f.splitlines())

    for i in my_new_list:
        i = ''.join(i)

        real_money = int(i.split(' - ')[1])
        worker = str.upper(i.split(' - ')[0])
        real_money = int(real_money - (real_money * 0.13))
        salary_dict = {}

        print('{} {}'.format(worker, real_money))
file.close()