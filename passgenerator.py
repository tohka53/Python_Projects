import random


largo_pass = int(input('De cuantos caracteres desea la contraseña?'))
specisim = int(input('Cuantos simbolos desea'))
cantidadnumeros = int(input('Cuantos numero desea'))

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number ="0123456789"
symbols =".#$%&/!@"

password=''

for char in range(1,largo_pass+1):
    random_char =random.choice(lower_case)
    

for char in range(1,cantidadnumeros+1):
    random_char =random.choice(number)
for char in range(1,largo_pass+1):
    random_char =random.choice(specisim)
    password += random_char
    print(f'{password}')
