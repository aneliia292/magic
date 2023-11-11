import random


class Solder:
    def __init__(self, name='noname', health=100):
        self.name = name
        self.health = health

    def set_name(self, name):
        self.name = name

    def make_kick(self, enemy):
        enemy.health -= random.randint(10, 20)
        if enemy.health < 0:
            enemy.health = 0
        self.health += 10
        print(f'{self.name} ударил {enemy.name}')
        print(f'{self.name} - {enemy.health} hp')


class Battle:

    def __init__(self, solder1, solder2):
        self.solder1 = solder1
        self.solder2 = solder2
        self.result = "Все только начинаеться"

    def battle(self):
        while self.solder1.health > 0 and self.solder2.health:
            n = random.randint(1, 2)
            if n == 1:
                self.solder1.make_kick(self.solder2)
            else:
                self.solder2.make_kick(self.solder1)

        if self.solder1.health > self.solder2.health:
            self.result = f'Победил {self.solder1.name}!'

        else:
            self.result = f'Победил {self.solder2.name}!'

    def who_won(self):
        print(self.result)


solder1 = Solder('solder1', 46)
solder2 = Solder()
solder2.set_name('solder2')
b = Battle(solder1, solder2)
b.battle()
b.who_won()