
def calcular_IMC(peso, alturaMetros):
   imc = peso/(alturaMetros*alturaMetros)
   return imc

def pedir_IMC():

    peso =float(input("Ingrese su peso en KG  "))
    altura =int(input("Ingrese su altura en CM  "))
    alturaMetros = altura/100
    imc = calcular_IMC(peso,alturaMetros)

    print("Su IMC es de "+ str(imc))
    if imc< 20:
        print("Estado de delgadez")
    if imc>= 20 and  imc < 26:
        print("Peso Normal")
    if imc >= 26 and imc < 30:
        print("Sobrepeso")
    if imc> 30:
        print("Obesidad")


print("Calcular IMC")
pedir_IMC()