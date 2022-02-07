from random import randint
def pos_neg (volume, water):
    if water > volume / 2:
        result = 'Стакан наполовину полон :)'
    elif water < volume / 2:
        result = 'Стакан наполовину пуст :('
    else:
        result = 'У стакана золотая середина :/'
    return (result)
volume = int(input('Введите объем стакана: '))
water = randint(0, volume)
print(f'Воды в стакане: {water}')
print (pos_neg (volume, water))