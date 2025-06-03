#Claves Fuertes

#Escriba un programa tn Python que solicite al usuario ingresar
#una contraseña y luego evalue su seguridad utilizando las siguientes reglas:

#1. la Contrasena debe tener por lo menos 8 caracteres
#2. Debe contener al menos una letra mayuscula y al menos una minuscula
#3. Debe contener un numero
#4. Debe contener al menor un caracter especial: !, #, @, $, %, etc.

def validar_password(password):
    if  len(password) <= 8:
        print("- Debe tener por lo menos 8 caracteres.\n")
        return False

    if not any(c.isupper() for c in password):
        print("- Debe contener por lo menos una mayúscula.\n")
        return False

    if not any(c.islower() for c in password):
        print("- Debe contener por lo menos una minúscula.\n")
        return False

    if not any(c.isdigit() for c in password):
        print("- Debe contener por lo menos un número.\n")
        return False

    if not any(c in "!@#$%^&*()_-+=<>?/{}[]|\\:;\\'`~,." for c in password):
        print("- Debe contener por lo menos un carácter especial.\n")
        return False

    return True

while True:
    password = input("Ingrese una contraseña: ")
    if validar_password(password):
        print("el password es seguro.")
        break
    else:
        print("Por favor, intente nuevamente.\n")
