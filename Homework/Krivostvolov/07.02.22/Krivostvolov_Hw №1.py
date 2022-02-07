def methods (centimetr, method):
    if method == 1:
        result = centimetr / 2.54
    elif method == 2:
        result = centimetr / 160934
    elif method == 3:
        result = centimetr / 185200
    elif method == 4:
        result = centimetr / 10
    else:
        result ='Error'
    return(result)
centimetr = float(input('Введит число в сантиметрах: '))
method = int(input('В какие единицы Вы хотите перевести сантиметры?\n1 - Дюймы\n2 - мили\n3 - морские мили\n4 - милиметры\nВвод: '))
print(f'Результат: {methods (centimetr, method)}')