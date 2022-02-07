from random import randint
def anomaly ():
    if num == 1:
        result = ('Вы нашли огненную аномалию')
    elif num == 2:
        result = ('Вы нашли электроаномалию')
    elif num == 3:
        result = ('Вы нашли токсичную аномалию')
    elif num == 4:
        result = ('Вы нашли гравианомалию')
    elif num == 5:
        result = ('Вы встретили призрака Гарика который сказал - Проходи не задерживайся')
    else:
        result = ('Вы ничего не нашли')
    return(result)
num = randint(1, 6)

print(f"Результаты ваших исследований {anomaly()}")