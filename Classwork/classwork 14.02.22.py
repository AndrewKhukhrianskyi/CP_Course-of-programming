# HW & CW 14.02.22
# Task 3 - Triangle function
def triangles(**triangle_pars):
    triangle_pars['name'] = 'Треугольник'
    triangle_list = list(triangle_pars.values())
    perimeter = 0
    
    if 0 < triangle_pars['angle'] < 90:
        triangle_pars['angle_type'] = 'Остроугольный'
    elif triangle_pars['angle'] == 90:
        triangle_pars['angle_type'] = 'Прямоугольный'
    elif 90 < triangle_pars['angle'] < 180:
        triangle_pars['angle_type'] = 'Тупоугольный'
    else:
        return 'Error'
    
    for side in range(3, len(triangle_list)):
        if type(triangle_list[side]) is int:
            perimeter += triangle_list[side]
            
    triangle_pars['perimeter'] = perimeter
    print(triangle_pars)


triangles(name = None, angle_type = None,
          angle = 90, side1 = 5, side2 = 12,
          side3 = 13, perimeter = None)

# Task 2 - Bug fix
def vowels_counter(sentence): 
    vowel_dict = 'аоеияюэыеу' 
    vowel_c_dict = {} 
    sentence = sentence.lower() 
    for elem in sentence: 
        if elem in vowel_dict: 
            vowel_c_dict[elem] = sentence.count(elem)           
    print(vowel_c_dict)

vowels_counter(input('Message: '))

          
      
