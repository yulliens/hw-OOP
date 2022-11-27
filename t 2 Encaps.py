"""
В классе Hero из предыдущего занятия добавьте приватное свойство rank.
Создайте геттер, сеттер и делиттер чтобы можно было получить звание героя, установить звание "Победитель арены"
в случае победы героя в битве и удалить ранк в случае поражения.
"""

class Hero:
    def __init__(self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
        self.__rank = None

    def print_info(self):
        print('Поприветствуйте героя ->', self.name)
        print('Уровень здоровья ->', self.health)
        print('Класс брони ->', self.armor)
        print('Сила удара ->', self.power)
        print('Оружие ->', self.weapon)


    def set_rank(self, win):
        if win:
            self.__rank = 'Победитель арены'


    def get_rank(self):
        return self.__rank


    def del_rank(self, lose):
        if lose:
            self.__rank = None

knight = Hero('Марк', 50, 25, 20, 'пистолет')
knight.print_info()
knight.set_rank(True)
print(knight.get_rank())
knight.del_rank(True)
print(knight.get_rank())
