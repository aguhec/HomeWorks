import os
import sys
import shutil
import os.path
import pathlib
import inspect

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


def make_folders():
    path = os.getcwd()
    folders = ['dir_' + str(i + 1) for i in range(9)]
    # full_path = os.path.join(path, f)

    for f in folders:
        full_path = os.path.join(path, f)
        if not os.path.exists(full_path):
            os.mkdir(full_path)


def del_folders():
    path = os.getcwd()
    folders = ['dir_' + str(i + 1) for i in range(9)]
    for f in folders:
        full_path = os.path.join(path, f)
        if os.path.exists(full_path):
            os.rmdir(full_path)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def show_folders():
    path = os.getcwd()
    for i in os.listdir(path):
        print(i)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


# Здесь я пытался найти путь до данного файла. Нашел этот способ. объясните его на уроке пожалуйста,
# current_file = inspect.getframeinfo(inspect.currentframe()).filename
# path1 = os.path.dirname(os.path.abspath(current_file))
# path = os.getcwd() Они одинаковые с path1

def copy_furrent_file():
    file = sys.argv[0]
    shutil.copyfile(file, file + '_copy.py')
######################################
# Функции для задания medium
def change_dir(path):
    try:
        os.chdir(path)
        print('Опп-па! Мы находимся по адресу: {}\n'.format(path))
    except FileNotFoundError:
        print('Хозяин, я боюсь такой папки нет :(\n')

def create_folder(new_folder):

    full_path = os.path.join(os.getcwd(), new_folder)
    if not os.path.exists(full_path):
        os.mkdir(full_path)
        print('Я создал для вас новую папочку (мимими)\n')
    else:
        print('Не могу, хозяин, такая папка уже есть.\n')
def remove_folder():

    path = os.getcwd()
    print('Папки доступные для удаления\n'
          '-----------------')
    for i in os.listdir(path):
        if os.path.isfile(i) is False:
            print(i)
    folder_name = input('Введите название папки, которую нужно удалить: ')
    full_path = os.path.join(path, folder_name)
    if os.path.exists(full_path):
        os.rmdir(full_path)
        print('Раньше тут была папка {}... теперь её нет:(\n'.format(folder_name))
    else:
        print('Не могу, хозяин, такой папки нет :((\n')