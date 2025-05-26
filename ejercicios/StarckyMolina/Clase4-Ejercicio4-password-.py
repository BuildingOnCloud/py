#Escribe un programa en Python que solicite al usuario ingresar una contraseña y luego evalúe su seguridad utilizando las siguientes reglas:

#1. La contraseña debe tener al menos 8 caracteres de longitud.
#2. Debe contener al menos una letra mayúscula y al menos una letra minúscula.
#3. Debe contener al menos un número.
#4. Debe contener al menos un carácter especial, como !, @, #, $, %, etc.

#El programa debe proporcionar un mensaje de retroalimentación al usuario, indicando si la contraseña es segura o no según estas reglas.

#Nota: Use la operacion input() para leer el ingreso de información.

# "!@#$%^&*()_-+=<>?/{}[]|\\:;\\'`~,." caracteres

while True:
    password = str(input("Ingrese su contraseña"))
    longitudPassword = len(password)

    caracterEsp = "!@#$%^&*()_-+=<>?/{}[]|\\:;\\'`~,."

    if longitudPassword >= 8:
        minusc = any(caracter.islower() for caracter in password)
        if minusc:
            mayusc = any(caracter.isupper() for caracter in password)
            if mayusc:
                numero = any(caracter.isdigit() for caracter in password)
                if numero:
                    #caracterEspSeparados = list(caracterEsp)
                    caracterEncontrado = any(caracter in caracterEsp for caracter in password)
                    if caracterEncontrado:
                        print("La contraseña esta correcta")
                        break
                    else:
                        print("contraseña no cumple con los requisitos de tener al menos un caracter especial de estos !@#$%^&*()_-+=<>?/{}[]|\\:;\\'`~,. ")  
                else:
                    print("contraseña no cumple con los requisitos de tener al menos un numero")
            else:
                print("contraseña no cumple con los requisitos de tener al menos una mayuscula")
        else:
            print("contraseña no cumple con los requisitos de tener al menos una letra minuscula")
    else:
        print("contraseña no cumple con los requisitos de al menor tener 8 caracteres")
