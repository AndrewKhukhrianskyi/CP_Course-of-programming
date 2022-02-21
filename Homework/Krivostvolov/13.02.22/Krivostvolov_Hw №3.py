def triangle (**triangle_opt):
    name = 'Треугольник'
    angle = int(input('Введите наибольший угол: '))
    if angle == 90:
        angle = 'Прямоугольный'
    elif 90 < angle < 180:
        angle = 'Тупоугольный'
    elif angle < 90 and angle > 0:
        angle = 'Остроугольный'
    else:
        angle = 'Error'
    massive_sides = []
    for i in range (3):
        i += 1
        sides = int(input(f"Введите сторону {i}: "))
        massive_sides.append(sides)
    perimetr = sum(massive_sides)
    triangle(figure_type = None, triangle_name = None, triangle_perimetr = None)
    triangle(figure_type = name, triangle_name = angle, triangle_perimetr = perimetr)
    return()
triangle()