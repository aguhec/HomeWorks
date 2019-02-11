# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

class TownCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car start')

    def stop(self):
        print('Car stop')

    def turn(self, direction):
        print('Car {} turn on {}'.format(self.name, direction))


class SportCar(TownCar):
    def __init__(self, speed, color, name, is_police=False):
        TownCar.__init__(self, speed, color, name)


class WorkCar(TownCar):

    def __init__(self, speed, color, name, is_police=False):
        TownCar.__init__(self, speed, color, name, is_police=False)


class PoliceCar(TownCar):

    def __init__(self, speed, color, name, is_police=False):
        TownCar.__init__(self, speed, color, name, is_police=True)


car_1 = TownCar('red', 'VAZ')
car_1.turn('left')