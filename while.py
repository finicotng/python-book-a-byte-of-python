number = 23
running = True

while running:
    guess = int(input('введите целое число : '))

    if guess == number:
        print('поздравляю, вы угадали')
        running = False
    elif guess < number:
        print('нет, загаданное число немного больше')
    else:
        print('нет, загаданное число немного меньше')
else:
    print('цикл while закончен')

print('завершение')