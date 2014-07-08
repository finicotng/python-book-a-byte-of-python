print('простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist  # mylist - ссылка на тот же объект в памяти

del shoplist[0]

print('shoplist', shoplist)
print('mylist', mylist)

# копирование при момощи полной вырезки
mylist = shoplist[:]
del shoplist[0]

print('shoplist', shoplist)
print('mylist', mylist)
