x = 50


def func(x):
    print('x равен', x)
    x = 2
    print('замена локального х', x)

func(x)
print('x по прежнему', x)