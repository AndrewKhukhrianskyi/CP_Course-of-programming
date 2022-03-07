# CW 07.03.22
"""
from random import choice

1. Отрисовать виселицу
2. Проверять правильность ответа
3. Рисовать части тела при неправильном ответе
4. Проверка на проигрыш
5. Вопросы

def draw_vic(arr):
    print('------------------')
    print(r'|                  /')
    print(f'|                 {arr[0]}')
    print(f'|                  {arr[1]}')
    print(f'|                  {arr[1]}')
    print(f'|                  {arr[2], arr[2], arr[1], arr[2], arr[2]}')
    print(f'|                  {arr[3], arr[3]}')
    print(f'|                  {arr[3], arr[3]}')
    print(f'|                  {arr[3], arr[3]}')
    print(f'____________________________')

def check_ans(ans): # dict {'Вопрос' : 'Ответ'}, keys(), values()
    if ans.lower() == 'плутон': 
        return True
    else:
        return False

def check_lose(arr):
    count = 0
    for elem in arr:
        if elem != '':
            count += 1
    if count == 9:
        print('Вы убили бедолагу своими ошибками :С')
    else:
        print("Бедняга будет жить! Вы молодец!")


body = ['O', '|', '-', '/'] # Переделать. Расширить список отдельно
tries = ['' for elem in range(9)] # Наши попытки, ex. tries = ['', '', ...]

for trying in range(len(tries)):
    print('Какая планета считается планетой-карликом? ') # Словарь (keys())
    ans = input('Ответ: ')
    if check_ans(ans): # check_ans(ans) == True:
        print("Верно!")
    else:
        print("Неверно!")
        tries[trying] = body[trying] # Ошибка индекса
        draw_vic(tries)

check_lose(tries)
"""
# Files
#file = open('file.txt', 'r') # Установили атрибут доступа и открыли файл
#data = file.read() # Читаем информацию (str)
#print(data)

#file.close() # Закрыли файл

file_w = open('file.txt', 'w')
file_w.write('ПОКА, МОЙ ДРУГ!')

file_w.close()

file_w = open('file.txt', 'r')
data_w = file_w.read()
print(data_w)

file_w.close()
