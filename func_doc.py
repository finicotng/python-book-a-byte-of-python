def print_max(x, y):
    """выводит максимальное из двух чисел.
Оба значения должны быть целыми, если возможно"""
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')

print(3, 5)
print(print_max.__doc__)