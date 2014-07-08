shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
name = 'swaroop'

# Индексирование
print('элемент 0 -', shoplist[0])
print('элемент 1 -', shoplist[1])
print('элемент 2 -', shoplist[2])
print('элемент 3 -', shoplist[3])
print('элемент -1 -', shoplist[-1])
print('элемент -2 -', shoplist[-2])
print('символ 0 -', name[0])

# вырезка из списка
print('элементы с 1 по 3:', shoplist[1:3])
print('элементы с 2 до конца:', shoplist[1:])
print('элементы с 1 по -1:', shoplist[1:-1])
print('элементы от начала до конца:', shoplist[:])

# вырезка из строки
print('символы с 1 по 3:', name[1:3])
print('символы с 2 до конца:', name[2:])
print('символы с 2 до -1:', name[1:-1])
print('символы от начала до конца:', name[:])

# множества
print('#####')
bri = {'бразилия', 'россия', 'индия'}  # set(['бразилия', 'россия', 'индия'])
print('индия' in bri)
print('сша' in bri)

bric = bri.copy()
bric.add('китай')
print(bric.issuperset(bri))

bri.remove('россия')
print(bri & bric)
# или то же самое
print(bri.intersection(bric))