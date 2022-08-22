from itertools import count
from tkinter import E


nombre_uno = input('Ingrese nombre uno')
nombre_dos = input('Ingrese nombre dos')

nombre_combinado = nombre_uno+nombre_uno

lower_case_string = nombre_combinado.lower()

t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')


true = t+r+u+e

l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')

love= l+o+v+e

love_score = int(str(true)+str(love))

if love_score <10 or love_score>90:
    print(f'Your love score is {love_score}')
elif love_score >=40 or love_score <= 50:
    print(f'Your score is {love_score} you alrigth')
else:
    print(f'Your score is {love_score}')