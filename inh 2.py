"""
Создайте класс который будет устанавливать свойство name и иметь метод
который к имени прибавляет надпись "гений". Создайте еще 1 класс, унаследуйте предыдущий.
Во втором классе вызовите метод класса родителя и добавьте к выводу надпись "но его отчислят если он не будет учить ООП".
Создайте экземпляр второго класса с вашим именем и вызовите метод печатающий всю надпись.
"""


class full_name:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"{self.name} гений")


class Name(full_name):
    def plus_print_info(self):
        print(f"{self.name} гений, но ее отчислят, если она не будет учить ООП.")

yulia = full_name("Юлия")
yulia.print_info()

yulia = Name("Юлия")
yulia.plus_print_info()