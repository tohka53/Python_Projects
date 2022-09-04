estatura = int(input('Ingrese su estatura en centimetros'))
bill= 0


if estatura >= 140:
    edad = int(input('ingrese edad'))
    if edad >= 19:
        print('Pague Q25.00')
        bill = 25
    else:
        print("Pague Q17.00")
        bill = 12
    ticket = input('Desea imprimier el ticket? Y o N')
    if ticket == 'y' or 'Y':
        bill = bill + 5
    
    print(f'Tu precio final es {bill}')

else:
    print('No puede ingresar')


