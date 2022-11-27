"""Класс ForeignPassport является производным от класса Passport. Метод PrintInfo
существует в обоих классах. PassportList представляет собой список, содержащий объекты
обоих классов. Вызов метода PrintInfo для каждого элемента списка демонстрирует его
полиморфное поведение."""

class Passport:
    def __init__(self, first_name, last_name, birthday, number, country):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.number = number
        self.country = country


    def print_info(self):
        print(self.first_name, self.last_name, self.birthday, self.number, self.country)


class foreignPassport(Passport):
    def __init__(self, first_name, last_name, birthday, number, country, visa):
        self.visa = visa
        super().__init__(first_name, last_name, birthday, number, country)


    def print_info(self):
        super().print_info()
        print(self.visa)


passportlist = []
foreignpassport = foreignPassport("Angella", "Jons", "25.06.2000", 678543, "Russia", "есть")
passportlist.append(foreignpassport)
passportlist.append(passport)
print(passportlist)
for i in passportlist:
    print()