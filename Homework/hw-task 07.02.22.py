# HW - Bug fix
def vowels_counter(sentence): # создаем ф-ю которая принимает одно слово
    vowel_dict = 'аоеияюэыеу' # словарь гласных букв
    vowel_c_dict = {} # словарь, который нужен для подсчета гласных букв
    value = 1 # Минимальное значение гласной буквы
    sentence = sentence.lower() # делает все слово\предложение с маленькой буквы.
    for elem in sentence: # перебираем каждый элемент в слове\предложении
        if elem in vowel_dict: # Если буква в словаре гласных букв
# Если нашей буквы не существует, то мы добавляем ее в словарь с минимальным значением (т.е 1), в противном случае - считаем повторения этих букв
            if elem not in vowel_c_dict: 
                vowel_c_dict[elem] = value
            else:
                vowel_c_dict[elem] = value + 1
                
    print(vowel_c_dict)
