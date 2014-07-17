class ShortInputException(Exception):
    """Поьлзовательский класс исключения"""
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Введите что-нибудь: ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('ну зачем вы сделали мне EOF?')
except ShortInputException as ex:
    print('ShortInputException: Длина введенной строки {0}; ожидалось, как минимум, {1}'.format(ex.length, ex.atleast))
else:
    print('исключений не было')
