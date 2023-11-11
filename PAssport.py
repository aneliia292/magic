class Passport:

    def __init__(self, first_name, last_name, date_of_birth, num_of_passport):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.num_of_passport = num_of_passport

    def printInfo(self):
        print(f'''
        Имя - {self.first_name}
        Фамилия - {self.last_name}
        Дата рождения - {self.date_of_birth}
        Номер паспорта - {self.num_of_passport}''')


class ForeignPassport(Passport):
    def __init__(self, first_name, last_name, date_of_birth, num_of_passport, country, visa):
        super().__init__(first_name, last_name, date_of_birth, num_of_passport)
        self.country = country
        self.visa = visa

    def printInfo(self):
        super().printInfo()
        print(f'        Страна {self.country}\n        Visa - {self.visa}')


def passport_list(obj):
    return obj.printInfo()


p1 = Passport('Ivan', 'Ivanov', '11/09/2007', '1234 345405')

fp = ForeignPassport('Petr', 'lustName', '12/23/4321', 'GDR3123', 'Russia', 'China')
passport_list(p1)
passport_list(fp)

pl = []
pl.append(p1)
pl.append(fp)
for passport in pl:
    passport_list(passport)

