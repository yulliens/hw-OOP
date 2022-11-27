"""
Создайте композицию User состояющую из:
Объекта Profile со свойствами: name,last_name,age,pasport и методом print_info.
Объекта Address со свойствами : City,street,zipcode
Объекта Role со свойствами: role,hours_worked
Объекта BankAccount со свойствами: card_number, balance
Объекта Order с методом устанавливающими параметры заказа: Item,date,delivery,price
Добавьте в композицию методы создания профиля, установки адреса, роли, привязки банковского аккаунта и добавления заказа
"""

class Profile:
    def __init__(self, name, last_name, age, pasport):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.pasport = pasport


    def print_info(self):
        print(self.name, self.last_name, self.age, self.pasport)


class Address:
    def __init__(self, city, street, zipcode):
        self.city = city
        self.street = street
        self.zipcode = zipcode


class Role():
    def __init__(self, role, hours_worked):
        self.role = role
        self.hours_worked = hours_worked


class BankAccount():
    def __init__(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance


class Order():
    def __init__(self, item, date, delivery, price):
        self.item = item
        self.date = date
        self.delivery = delivery
        self.price = price

