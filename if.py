number = 23
guess = int(input('Введите целое число : '))

if guess == number:
    print('поздравляю, вы угадали,')
    print('(хотя и не выиграли никакого приза!)')
elif guess < number:
    print('нет, загаданное число немного больше этого')
else:
    print('нет, загаданное число немного меньше этого')

print('завершено')