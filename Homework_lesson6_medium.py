import random


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _income_damage(self, damage):
        if self.armor > 0:
            self.armor = self.armor - int(damage * random.uniform(0.1, 1.0))
            if self.armor <= 0:
                self.armor = 0
        else:
            self.health = self.health - int(damage * random.uniform(0.1, 1.0))
            if self.health <= 0:
                self.health = 0

        print('{} получил урон и теперь имеет {} здоровья, {} армора'.format(self.name, self.health, self.armor))

    def punch(self, person):
        person._income_damage(self.damage)


class Player(Person):
    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)


class Enemy(Person):
    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)


class Fight:
    def __init__(self, person1, person2):
        self.person1 = person1
        self.person2 = person2

    def start(self, person1, person2):
        while person1.health > 0 and person2.health > 0:
            person1.punch(person2)
            if person2.health == 0:
                print('{} победил!'.format(person1.name))
                break
            person2.punch(person1)
            if person1.health == 0:
                print('{} победил!'.format(person2.name))


player = Player('DARTH VADER ', 100, 10, 50)
enemy = Enemy('Luke Skywalker', 100, 10, 50)

new_fight = Fight(player, enemy)
new_fight.start(player, enemy)
