# Homework 31.01.22
# Task 1 - Кирпич
def calculate_bricks(brick_weight, max_weight):
    print(f"Кол-во кирпичей= {max_weight // brick_weight}шт")


# Task 2 - Anomalies
from random import randint
def check_anomaly():
    num = randint(1,5)
    if num == 1:
        print('Огненная аномалия')
    elif num == 2:
        print('Электроаномалия')
    elif num == 3:
        print('Аномалия "Карусель"')
    elif num == 4:
        print('Пси-аномалия')
    else:
        print('Вы встретили мутанта')

# Task 3 - odd words
def odd_words(word):
    odd_word = ''
    try:
        for letter in range(len(word)):
            if letter % 2 != 0:
                odd_word += word[letter]
    except:
        print('Деление на ноль')

    print(odd_word)
    
# Classwork 31.01.22
#def f(a = 1, b):
#    print(a + b)

def more_var(*args):
    for arg in args:
        print(arg)

more_var(1,2,3,4,5,6,1,2,3,4,5,6)
