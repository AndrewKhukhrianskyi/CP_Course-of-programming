# Homework 07.02.22
# Task 1 - Length converter
def l_converter(cm):
    len_list = ['д', 'мл', 'ммл', 'мм']
    values = [2.54, 160934, 185200, 10]
    for elem in range(len(len_list)):
        print(f"Результат: {cm / values[elem], len_list[elem]}")

#l_converter(1500)
# Task 2 - Vowel Counter
# HW - Bug fix
def vowels_counter(sentence):
    vowel_dict = 'аоеияюэыеу'
    vowel_c_dict = {}
    value = 1
    sentence = sentence.lower()
    for elem in sentence:
        if elem in vowel_dict:
            if elem not in vowel_c_dict:
                vowel_c_dict[elem] = value
            else:
                vowel_c_dict[elem] = value + 1
                
    print(vowel_c_dict)

#vowels_counter('Шла Саша по шоссе и сосала сушку')

# Task 3 - Glass optimism
from random import randint
#glass_volume = int(input('Enter glass volume: '))

def glass_checker(ml, glass_volume):
    if ml > glass_volume // 2:
        print(True, ml)
    elif ml < glass_volume // 2:
        print(False, ml)
    else:
        print(None, ml)
        
#glass_checker(randint(10, glass_volume), glass_volume)
# Classwork 07.02.22
def func(*userdata):
    for elem in userdata:
        print(elem)
        
    print(type(userdata))
#func('Andy', 'Anderson', 25, 'Male',
#     'Married', '5000$', 'Fishing')

def kwargs(**userdata):
    print(userdata)

#kwargs(name = 'Andy', surename = 'Anderson')

def func(a1, a2):
    print(a1 + a2)
func(1, 2)
func('a', 'b')

'''
HW task
Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.

For example: ["3:1", "2:2", "0:1", ...]

Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:

if x>y - 3 points
if x<y - 0 point
if x=y - 1 point
Notes:

there are 10 matches in the championship
0 <= x <= 4
0 <= y <= 4
'''



