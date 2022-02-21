# +, -, *, /, //
# input()
#n1 = int(input('Ч1:  '))
#n2 = int(input('Ч2: '))
#print(n1 + n2)
# Homework 20.02.22
# Task 1 - Operator

def operator(phone):
    if phone == '':
        print('Ошибка: Ничего не введено! ')
        return ''
    
    kievstar = '067068097'
    mts = '066096'
    life = '063073'
    if phone[0:3] in kievstar:
        print('Номер киевстаровский!')
    elif phone[0:3] in mts:
        print('MTS')
    elif phone[0:3] in life:
        print('Life :)')
    else:
        print('Неизвестный оператор')

# operator(input('Number: '))
# Task 2 - Square sum
def square_sum(*numbers):
    list_num = list(numbers)
    for elem in range(len(list_num)):
        list_num[elem] **= 2
    print(list_num)
    print(sum(list_num))
#square_sum(1,2,3, 5 -3, 12)

# Classwork 21.02.22
def to_list(*data):
    return list(data)

def filter_data(arr):
    numbers = []
    for elem in arr:
        if type(elem) is int:
            numbers.append(elem)

    return numbers

def odd_even(arr):
    odd = []
    even = []
    for elem in arr:
        if elem % 2 == 0:
            even.append(elem)
        else:
            odd.append(elem)
    print(odd)
    print(even)
    return 'Even', sum(even), 'Odd', sum(odd)


#print(odd_even(filter_data(to_list('hello', 'user', 4, 2, 2, 7, 9, 'dom', '15132521tfds', 3, 11, 1))))



