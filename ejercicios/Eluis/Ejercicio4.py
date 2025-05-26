#Escribe un programa en Python que solicite al usuario ingresar una contraseña y luego evalúe su seguridad utilizando las siguientes reglas:

#1. La contraseña debe tener al menos 8 caracteres de longitud.
#2. Debe contener al menos una letra mayúscula y al menos una letra minúscula.
#3. Debe contener al menos un número.
#4. Debe contener al menos un carácter especial, como !, @, #, $, %, etc.

#El programa debe proporcionar un mensaje de retroalimentación al usuario, indicando si la contraseña es segura o no según estas reglas.

#Nota: Use la operacion input() para leer el ingreso de información.

# "!@#$%^&*()_-+=<>?/{}[]|\\:;\\'`~,." caracteres


#Importo funcion :  Esta es una constante predefinida en 
#el módulo string que contiene una cadena con todos los caracteres especiales o signos de puntuación comunes
#Defino mis variables:

#Defino mis variables:

password = str(input("Ingrese Password:   "))
passworlongitud = len(password)
minuscula = any(caracter.islower() for caracter in password)
mayuscula = any(caracter.isupper() for caracter in password)
numero = any(caracter.isdigit() for caracter in password)
caracteres_especiales = "!@#$%^&*()_-+=<>?/{}[]|\\:;\\'`~,."
caracterEspecial = any(caracter in caracteres_especiales for caracter in password)

#Creo estructuras y operaciones para las reglas del password:

if passworlongitud >= 8:
    if minuscula:
        if mayuscula:
            if numero:
                if caracterEspecial:
                    print("Password Cumple con todos los requisitos.")
                else:
                    print("Password no cumple con los requisitos; debe contener al menos un carácter especial, como !, @, #, $, %, etc")
            else:
                print("Password no cumple con los requisitos; debe contener al menos un número")


        else:
            print("Password no cumple con los requisitos; debe contener al menos una letra mayúscula")

    else:
        print("Password no cumple con los requisitos; debe contener al menos una letra minúscula")
else:
    print("Password no cumple con los requisitos; debe contener al menos 8 caracteres de longitud")