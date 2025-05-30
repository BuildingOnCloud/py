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