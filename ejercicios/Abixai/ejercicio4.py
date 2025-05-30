#Escribe un programa en Python que solicite al usuario ingresar una contraseña y luego evalúe su seguridad utilizando las siguientes reglas:

#1. La contraseña debe tener al menos 8 caracteres de longitud.
#2. Debe contener al menos una letra mayúscula y al menos una letra minúscula.
#3. Debe contener al menos un número.
#4. Debe contener al menos un carácter especial, como !, @, #, $, %, etc.

#El programa debe proporcionar un mensaje de retroalimentación al usuario, indicando si la contraseña es segura o no según estas reglas.

#Nota: Use la operacion input() para leer el ingreso de información.

# "!@#$%^&*()_-+=<>?/{}[]|\\:;\\'`~,." caracteres


password = input("Ingrese su contraseña: ")

longitud = len(password)
symb = "!@#$%^&*()_-+=<>?/{}[]|\\:;\\'`~,."
if longitud>=8:
    minus = any(caracter.islower() for caracter in password)
    mayus = any(caracter.isupper() for caracter in password)
    numero = any(caracter.isdigit() for caracter in password)
    

    if minus == True and mayus == True and numero == True:
        for caracter in password:
            if caracter in symb:
                print('La contrasena cumple con los requisitos')
                break
    else:
        print('Error: Contrasena no cumple los requisitos') 
else:
    print('Error: Contrasena no cumple los requisitos') 