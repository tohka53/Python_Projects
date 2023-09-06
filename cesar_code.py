abecedario= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

direction= input("Ingrese si decesa encrypt(e) o decode(d):\n")
text =input("Ingrese codigo:\n")
shift = (int(input("Ingrese el shift number\n")))



def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position =abecedario.index(letter)
        new_position = position +shift_amount
        new_letter = abecedario[new_position]
        cipher_text += new_letter
        print(f"El encriptado es {cipher_text}")


 
def decode(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position =abecedario.index(letter)
        new_position = position -shift_amount
        new_letter = abecedario[new_position]
        cipher_text += new_letter
        print(f"El encriptado es {cipher_text}")


if direction =='e':
    encrypt(plain_text=text, shift_amount=shift)
    
elif direction =='d':
    decode(plain_text=text, shift_amount=shift)

