def triangle (**triangle_opt):
    name = 'Треугольник'
    angle = int(input('Введите наибольший угол: '))
    if angle == 90:
        angle = 'Прямоугольный'
    elif angle > 90 and angle < 180:
        angle = 'Тупоугольный'
    elif angle < 90 and angle > 0:
        angle = 'Остроугольный'
    else:
        angle = 'Error'
    sides = []
    for i in range (3):
        i += 1
        sides.append = int(input(f"Введите сторону {i}: "))
    perimetr = sum(sides)
    result = f"Фигура {name}, Тип {angle}, Периметр {perimetr}"
    print(result)