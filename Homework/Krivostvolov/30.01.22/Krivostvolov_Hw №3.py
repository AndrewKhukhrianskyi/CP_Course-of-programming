def result (word):
    for i in range (word[-1]):
        new_word = f"{word[0: -1]} + {word[i+1: -1]}"
    return(new_word)
word = input('Введите слово: ')

print(result(word))