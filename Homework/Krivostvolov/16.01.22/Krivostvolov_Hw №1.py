print('Примечание.\n1 - программа будет работать только при 2 известных значениях\n2 - вводить только числа')
s = input('Введите расстояние: ')
v = input('Введите скорость: ')
t = input('Введите время: ')
if s == '':
    s = int(v)*int(t)
    print(f"Расстояние равно: {s}")
elif v == '':
    v = int(s)//int(t)
    print(f"Скорость равна: {v}")
elif t == '':
    t = int(s)//int(v)
    print(f"Время равно: {t}")
else:
    print('Прочитайте примечание')