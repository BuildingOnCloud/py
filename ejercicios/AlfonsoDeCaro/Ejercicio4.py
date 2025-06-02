import string

def es_segura(contrasena):
    # Regla 1: al menos 8 caracteres
    if len(contrasena) < 8:
        return False

    # Regla 2: al menos una letra mayúscula y una minúscula
    tiene_mayuscula = any(c.isupper() for c in contrasena)
    tiene_minuscula = any(c.islower() for c in contrasena)
    if not (tiene_mayuscula and tiene_minuscula):
        return False

    # Regla 3: al menos un número
    tiene_numero = any(c.isdigit() for c in contrasena)
    if not tiene_numero:
        return False

    # Regla 4: al menos un carácter especial
    caracteres_especiales = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~"
    tiene_especial = any(c in caracteres_especiales for c in contrasena)
    if not tiene_especial:
        return False

    return True

print("Por favor, ingresa una contraseña Segura:")

while True:
    contrasena = input("Contraseña: ")
    if es_segura(contrasena):
        print("¡La contraseña es segura!")
        break
    else:
        print("La contraseña no cumple con los requisitos. Debe de contener minimo 8 caracteres como Mayusculas, minusculas, numeros y caracteres especiales.")