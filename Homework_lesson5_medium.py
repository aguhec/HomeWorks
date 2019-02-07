# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os, sys, shutil, time
import Homework_lesson5_easy    #Почему это не сработало????

print('Вас приветствует ваш покорный слуга')
time.sleep(1)
print('Я помогу вам работать с файлами и папками....')

def start():
    try:
        choice_user = int(input('Выберите пункт из данного меню или что мне для Вас, мой господин, сделать?\n'
                            '[1] - Перейти в папку\n'
                            '[2] - Просмотреть содержимое текущей папки\n'
                            '[3] - Удалить папку\n'
                            '[4] - Создать папку\n'
                            '____________________\n'
                            'Ваш выбор: '))


        if choice_user == 2:
            from Homework_lesson5_easy import show_folders

            show_folders()
            start()

        elif choice_user == 1:
            new_path = input('Введите путь к необходимой папке: ')
            from Homework_lesson5_easy import change_dir

            change_dir(new_path)
            start()
        elif choice_user == 4:
            from Homework_lesson5_easy import create_folder

            new_folder = input('Давайте придумаем имя новой папке: ')
            create_folder(new_folder)
            start()
        elif choice_user == 3:
            from Homework_lesson5_easy import remove_folder
            remove_folder()
            start()
        else:
            print('Хозяин, введите пожалуйста цифры согласно меню.')
            start()
    except ValueError:
        print('Хозяин, введите пожалуйста цифры согласно меню.')
        start()
start()