class Equikment:

    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def action(self):
        return 'не определена'

    def __str__(self):
        return f'{self.name}, {self.make}, {self.year}'

class Printer(Equikment):

    def __init__(self, name, make, year, series):
        super().__init__(name, make, year)
        self.series = series

    def action(self):
        return 'печатает'

    def __str__(self):
        return f'{self.series}, {self.name}, {self.make}, {self.year}'

class Scaner(Equikment):

    def action(self):
        return 'сканирует'


class Xeroxs(Equikment):

    def action(self):
        return 'сканирует'

sklad = []
eq = Printer('Samsung', 'LP-222', 2022, 411512)
sklad.append(eq)
s = Scaner('Samsung', 'LP-128', 2023)
sklad.append(s)
x = Xeroxs('Danya', '6', 1978)
sklad.append(x)
print('На складее имеется:')
# for item in sklad:
    # print(item)
    # print(item.action())

for item in sklad:
    if isinstance(item, Printer):
        print(item)