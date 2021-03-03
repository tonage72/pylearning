def eat(food=None, happy=False):
    if happy:
        print('Yayyyy!!!')
    if food is None:
        print('Nom nom!!!')
    else:
        print('I had some {}.'.format(food))

eat('cheese', True)
eat()