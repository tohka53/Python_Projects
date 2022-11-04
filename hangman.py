#Step 1 

word_list = ["papel", "arbol", "camello"]


import random

palabra = random.choice(word_list)
print(f'La palbra a encontrar es: {palabra}')


guess = input('Guess a letter: ').lower()

for letter in palabra:
    if letter == guess:
        print('Correcto')
    else:
        print('Incorrecto')