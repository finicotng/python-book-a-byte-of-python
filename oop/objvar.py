class Robot:
    """Представляет робота с именем"""
    # переменная класса, содержащая количество роботов
    population = 0

    def __init__(self, name):
        """Инициализация данных"""
        self.name = name
        print('(инциализация {0})'.format(self.name))

        # при создании этой личности, робот добавляется
        # к переменной 'population'
        Robot.population += 1

    def __del__(self):
        """Я умираю"""
        print('{0} уничтожается'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} был последним'.format(self.name))
        else:
            print('осталось {0:d} работающих роботов'.format(Robot.population))

    def say_hi(self):
        """Приветствие"""
        print('приветствую! мой маста называет меня {0}'.format(self.name))

    @staticmethod
    def how_many():
        """Выводит численность роботов"""
        print('У нас {0:d} роботов'.format(Robot.population))

    # how_many = staticmethod(how_many) - делает то же самое

droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('C-3PO')
droid2.say_hi()
Robot.how_many()

print('здесь роботы могут что-то сделать')
print('роботы закончили работать. надо их уничтожить')

del droid1
del droid2

Robot.how_many()