while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('слишком мало')
        continue
    print('введенная строка достаточной длины')