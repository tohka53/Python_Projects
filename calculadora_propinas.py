
from re import X


monto = float(input('Ingrese monto total'))
porcentaje = int(input('Ingrese porcentaje de propina'))
personas = int(input('Cantidad de personas a pagar'))

propina = float(porcentaje)/100 + 1

total = (monto*propina/personas)

print((total))