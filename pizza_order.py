from tkinter.tix import InputOnly


pizza_size = input('Que tamanio desea la Pizza S, M or L')

precio = 0


if pizza_size =="S" or "s":
    precio = 50
    extra_queso = input('Desea queso extra? Y or N')
    if extra_queso == "Y" or "y":
        precio = precio +5
        extra_peperoni = input('Desea extra Peperoni? Y or N')
        if extra_peperoni == "Y" or "y":
            precio = precio + 5
            print('El total es' + str(precio))
        else:
          print('El total es' + str(precio))
    if extra_queso == "n" or "N":
        
        extra_peperoni = input('Desea extra Peperoni? Y or N')
        if extra_peperoni == "Y" or "y":
            precio = precio + 5
            print('El total es' + str(precio))
        else:
           print('El total es' + str(precio))
else:
    print('El total es' + str(precio))



if pizza_size == "M" or "m":
    precio = 70
if pizza_size == "L" or "l":
    precio == 90

