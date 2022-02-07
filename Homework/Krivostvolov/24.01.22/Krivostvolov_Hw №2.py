word = input('Введите слово: ')
choose = int(input('К какой букве Вы хотите обратиться? '))
try:
    print(word[choose])
except:
    print('Ошибка. Такой буквы нет. Попробуйте ещё раз')