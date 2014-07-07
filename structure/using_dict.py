ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print('адрес Swaroop\'a:', ab['Swaroop'])

# удаление ключа
del ab['Spammer']

print('\nВ адресной книге {0} контактов\n'.format(len(ab)))

for name, address in ab.items():
    print('контакт {0} с адресом {1}'.format(name, address))

# добавление ключа
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print('\nадрес Guido:', ab['Guido'])
