nombre = input("Ingrese su nombre  ")
print("Hola " + nombre)
edad = int(input("Ingrese su edad  "))
masDe12 = edad >= 12
respuesta_hijo = input("Es Hijo del Dueño  ")
hijo_del_dueño = respuesta_hijo =="si"

puede_pasar =masDe12 or hijo_del_dueño

if edad > puede_pasar:
    print("Puede Ingresar a la montraña rusa")
else:
    print("Puede Ingresar a la montraña rusa")