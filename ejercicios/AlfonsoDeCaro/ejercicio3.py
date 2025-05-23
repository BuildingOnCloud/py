def obtener_numero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            numero = float(entrada)
            return numero
        except ValueError:
            print("Por favor, ingresa un número válido.")

def main():
    print("programa para realizar operaciones básicas.")
    
    # Obtener los dos números con validación
    num1 = obtener_numero("Ingresa el primer número: ")
    num2 = obtener_numero("Ingresa el segundo número: ")
    
    # Mostrar opciones de operación
    print("Selecciona la operación que deseas realizar:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    
    while True:
        operacion = input("Ingresa el número de la operación (1/2/3/4): ")
        if operacion in ['1', '2', '3', '4']:
            break
        else:
            print("Por favor, ingresa una opción válida (1, 2, 3 o 4).")
    
    # Realizar la operación
    if operacion == '1':
        resultado = num1 + num2
        simbolo = '+'
    elif operacion == '2':
        resultado = num1 - num2
        simbolo = '-'
    elif operacion == '3':
        resultado = num1 * num2
        simbolo = '*'
    else:
        # Validar división por cero
        if num2 == 0:
            print("Error: No se puede dividir entre cero.")
            return
        resultado = num1 / num2
        simbolo = '/'
    
    # Mostrar el resultado
    print(f"El resultado de {num1} {simbolo} {num2} es: {resultado}")

if __name__ == "__main__":
    main()