numeros = {
    "0": "Cero",
    "1": "Uno",
    "2": "Dos",
    "3": "Tres",
    "4": "Cuatro",
    "5": "Cinco",
    "6": "Seis",
    "7": "Siete",
    "8": "Ocho",
    "9": "Nueve"    
}

texto= input("Ingrese un numero")

texto_final =""
for letra in texto:
    texto_final += numeros[letra] + " "
    
print(texto_final)