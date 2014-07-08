name = 'Swaroop'

if name.startswith('Swa'):
    print('да, стока начинается на "Swa"')

if 'a' in name:
    print('да, она содержит строку "a"')

if name.find('war') != -1:
    print('да, она содержит строку "war"')

delimeter = '_*_'

mylist = ['бразилия', 'россия', 'индия', 'китай']
print(delimeter.join(mylist))
