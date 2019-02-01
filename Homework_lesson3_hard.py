import random
import math
import time
import os


def attack(striker, defender):
    if ready == 'y':
        # while defender['health'] > 0:
        if random.randrange(0, 100) < defender['dodge']:
            print('Увы, промах')
        else:
            if random.randrange(0, 100) < defender['critical']:
                damage_in_armor(striker)
                striker['damage'] = striker['damage'] * 2
                defender['health'] = defender['health'] - striker['damage']
                striker['damage'] = striker['damage'] / 2
                print('-{} хп. Критический удар! У противника осталось {} хп'.format(int(striker['damage'] * 2),
                                                                                     int(defender['health'])))
            else:
                damage_in_armor(striker)
                defender['health'] = defender['health'] - striker['damage']
                print('-{} хп. У противника осталось {} хп'.format(int(striker['damage']),
                                                                   int(defender['health'])))
    return defender['health']


def damage_in_armor(striker):
    chance_of_armor = 15
    if random.randrange(0, 100) < chance_of_armor:
        striker['damage'] = math.trunc(striker['damage'] * 0.8)
    return striker['damage']


def good_luck():
    print('Вы выбрали {}а отличный выбор! удачи!'.format(race))


def stats(dict, new_dict):
    new_dict = {'health': (int(dict['stamina']) * 30), 'damage': (int(dict['str']) * random.randrange(3, 7)),
                'dodge': (int(dict['agility']) * 4), 'critical': (int(dict['intuition']) * 3)}
    return new_dict


dict_human = {'stamina': 5, 'str': 5, 'agility': 5, 'intuition': 5}
dict_orc = {'stamina': 5, 'str': 7, 'agility': 2, 'intuition': 6}
dict_elf = {'stamina': 4, 'str': 3, 'agility': 7, 'intuition': 6}
dict_dwarf = {'stamina': 8, 'str': 5, 'agility': 1, 'intuition': 6}
dict_enemy = {'stamina': 4, 'str': 4, 'agility': 3, 'intuition': 4}
new_enemy_stats = {}
enemy_stats = (stats(dict_enemy, new_enemy_stats))
target = ['по голове', 'в печень', 'в солнечное сплетение', 'по правому уху']
enemy_list = ['Коварный Гром', 'Краснобородый коротышка', 'Смертоносный Джо', 'Лопоухий Кривоглаз', 'Смердящий Хряк', ]
print('Добро пожаловать в прототип World of LineAge v.0.0.0.0.0.01')
race_choice = int(input('Выберите рассу вашего персонажа [1]Человек [2]Эльф [3]Орк [4]Гном\n\
Расы отличаются друг от друга параметрами.\n\
Так например орки сильны, эльфы ловки, а у гномов много здоровья\n\
Введите номер: '))
name = input('Как Вас будут называть в этом мире полном крови и невежества? ')
step = 0

player_dict = {}

if race_choice == 1:
    race = 'Человек'
    player_stats = (stats(dict_human, player_dict))
elif race_choice == 2:
    race = 'Эльф'
    player_stats = (stats(dict_elf, player_dict))
elif race_choice == 3:
    race = 'Орк'
    player_stats = (stats(dict_orc, player_dict))
else:
    race = 'Гном'
    player_stats = (stats(dict_dwarf, player_dict))

good_luck()
print('{} появился из неоткуда. и звали его никак. шучу... Имя его было {}... '
      'Только он появился в деревне, как на него напали '.format(race, name))
time.sleep(1)
enemy = enemy_list[random.randrange(0, 4)]
print('Это был инопланетный воин', enemy)
time.sleep(1)
ready = input('Предалагаю его огреть по голове... в конце концов это наша планета, согласны? y/n?')
if ready == 'y':
    print(name, 'наносит удар', target[random.randrange(0, 3)])
    attack(player_stats, enemy_stats)
    time.sleep(2)
    print(enemy, 'наносит удар', target[random.randrange(0, 3)])
    attack(enemy_stats, player_stats)
else:
    print('Таких трусов еще поискать надо.... досвидули')
    exit()

while enemy_stats['health'] > 0 and player_stats['health'] > 0:
    ready = input('Вмажем еще разок?')
    if ready == 'y':
        print(name, 'наносит удар', target[random.randrange(0, 3)])
        attack(player_stats, enemy_stats)
        time.sleep(2)
        print(enemy, 'наносит удар', target[random.randrange(0, 3)])
        attack(enemy_stats, player_stats)
    else:
        print('{} обявлен трусом! беги беги!!!! '.format(name))
        exit()
if enemy_stats['health'] <= 0:
    print('Победа!!! Наша планета может спать спокойно. до встречи в новой версии World of LineAge')
    exit()
elif player_stats['health'] <= 0:
    print('{}... ты пал смертью храбрых! И сейчас уже пируешь в вальгалле с праотцом!'.format(name))
    exit()
