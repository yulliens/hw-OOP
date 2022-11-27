"""
Создайте класс банковского аккаунта по аналогии с примером из презентации. Сделайте атрибут name защищенным, а
balance и pasport приватными.
Добавьте геттер-методы на pasport и balance. Сделайте смену номера паспорта по поролю. А изменение баланса
на определенную сумму(сумма не может падать меньше 0, так что сделайте проверку).
Создайте метод удаляющий паспортные данные с аккаунта(также по поролю).
"""
class bank_account:
    def __init__(self, name, balance, pasport, password):
        self._name = name
        self.__balance = balance
        self.__pasport = pasport
        self.__password = password

    def printdata(self):
        print(self._name, self.__balance, self.__pasport)


    def gett_balance(self):
        return self.__balance


    def gett_pasport(self):
        return self.__pasport


    def set_pasport(self, new_pasport, password):
        if password == self.__password:
            self.__pasport = new_pasport
            print('Паспортные данные успешно изменены')
        else:
            print('Пароль неверный')


    def set_balance(self, value):
        if self.__balance + value < 0:
            print('Недостаточно средств')
        else:
            self.__balance += value
            print('Транзация успешно завершена. Текущий баланс:', self.__balance)


    def del_pasport(self, password):
        if password == self.__password:
            self.__pasport = None
            print('Паспортные данные успешно удалены')
        else:
            print('Пароль неверный')


account = bank_account('Юлия', 1200, 657489, 1234)
account.printdata()
account.set_pasport(13547, 5678)
account.set_balance(-1500)
account.set_balance(50)