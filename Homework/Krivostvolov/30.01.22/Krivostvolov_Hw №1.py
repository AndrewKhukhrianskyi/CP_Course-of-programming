def result (max_weight, bricks_weight):
    return(max_weight//bricks_weight)

max_weight = int(input('Введите максимальный переносимый вес: '))
bricks_weight = int(input('Введите вес одного кирпича: '))

print(f'Можно перенести {result(max_weight, bricks_weight)} кирпичей')