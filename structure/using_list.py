# это мой список покупок
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']

print('я должен сделать', len(shoplist), 'покупок')

print('Покупки:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nТакже нужно купить риса.')
shoplist.append('рис')
print('теперь мой список покупок таков:', shoplist)

print('отсортирую-ка я свой список')
shoplist.sort()
print('отсортированный список покупок выглядит так:', shoplist)

print('первое, что мне нужно купить - это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('я купил', olditem)
print('теперь мой список покупок:', shoplist)
