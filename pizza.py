
size = input('Que tamanio desea la Pizza S, M or L')
add_pepperoni = input('Desea queso extra? Y or N')
extra_cheese = input('Desea queso extra? Y or N')
price= 0;

if size == "S" or "s": 
    price = 15 
    if add_pepperoni == "Y" or "y": 
        price += 2 
    if extra_cheese == "Y" or "y":
        price += 1 
elif size == "M" or "m": 
    price = 15 
    if add_pepperoni == "Y" or "y":
        price += 2 
    if extra_cheese == "Y" or "y":
        price += 1 

elif size == "L" or "l": 
    price = 15 
    if add_pepperoni == "Y" or "y":
        price += 2 
    if extra_cheese == "Y" or "y":
        price += 1 

print(f"Your final bill is: ${price}.")

