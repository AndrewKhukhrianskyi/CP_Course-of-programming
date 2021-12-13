'''
Homework 6.12.21
# Task 1 - Even numbers
list_num = []

for elem in range(1,10,2):
    list_num.append(elem)


print(list_num)

# Task 2 - Borders

from random import randint
from math import sqrt

arr = []
res = 0
for elem in range(1,10):
    arr.append(randint(0,10))


# Trick
arr.sort()
for elem in arr:
    if elem == 1:
        res += 1

print(arr)
print(f"Ones: {res}")

# Task 3 - Geometry (Triangles)

tr_amount = int(input('Amount of triangles: '))
res_arr = []

for elem in range(tr_amount):
    side_1 = int(input('Side 1: '))
    side_2 = int(input('Side 2: '))
    side_3 = int(input('Side 3: '))
    # Stewart theorem
    result = (sqrt(2 * side_1 ** 2 + 2 * side_2 ** 2 - side_3 ** 2)) / 2
    res_arr.append(result)

res_arr.sort()
print(res_arr)

# Task 4 - Messages and converts

tries = int(input('Amount of tries: '))
status = []

for elem in range(tries):
    s1 = randint(5,20) * randint(5,20)
    s2 = randint(5, 20) * randint(5,20)
    if s1 < s2:
        print(f"Element 1: {s1}, Element 2: {s2}")
        status.append(True)
    else:
        print(f"Element 1: {s1}, Element 2: {s2}")
        status.append(False)
print(status)
# Task 5 - Bubble sort
numbers = []

for elem in range(randint(3,10)):
    numbers.append(randint(1,10))

print(numbers)
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)





a = [[1, 2, 3, 'abc', 5, 6, 'hello'], ['go', 14, 'and', 15]]
strings = []
integers = []

for arr in a:
    for elem in arr:
        if type(elem) is int:
            integers.append(elem)
        else:
            strings.append(elem)

print(strings)
print(integers)
'''

from random import randint
numbers = []
results = []



for elem in range(randint(3,20)):
    numbers.append(randint(1,100))
    
print(numbers)

for num in numbers:
    if num % 5 == 0:
        results.append(num)

print(results)


