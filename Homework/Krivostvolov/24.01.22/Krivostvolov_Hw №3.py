end = ''
num_1 = int(input('Введите первое число: '))
while end != 'exit':
    num_2 = int(input('Введите второе число: '))
    result = num_1 + num_2  
    print(result)
    end = input('Введите exit для окончания программы: ')
    num_2 = int(input('Введите второе число: '))
    try:
        result += num_2
    except:
        result ='Ошибка. Введено не число'
    print(result)