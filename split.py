from unicodedata import name

import random
nombres_listado = input("Ingrese el listado de nombre de personas listados por comas y un espacio como se muestra en el ejemplo: Miguel, Eduardo, Juan")

names= nombres_listado.split(", ")
total_nombre = len(names)
random_name = random.randint(0, total_nombre-1)
print(names[random_name])