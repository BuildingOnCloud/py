# Ejercicio
# Calculadora con Manejo de Excepciones y Módulos
#
# Cree una calculadora simple que realice las operaciones de suma, resta, multiplicación y división.
# La calculadora debe permitir al usuario ingresar dos números y seleccionar la operación deseada.
# Además, debes manejar las siguientes situaciones con excepciones:
#
# 1. Manejar una excepción ValueError si el usuario ingresa algo que no sea un número.
# 2. Manejar una excepción ZeroDivisionError si el usuario intenta dividir por cero.

from modulo_operaciones import suma, resta, multiplicacion, division

while True:

    print("\nElija una opcion: ")
    print("1. Suma (+) ")
    print("2. Resta (-) ")
    print("3. Multiplicacion (*) ")
    print("4. Division (/)")
    print("5. Salir")
    opcion = input("\nSeleccione la operacion a realizar: ")

    if opcion == "5":
        print("\nSaliendo de la calculadora...")
        break
    if opcion not in ["1", "2", "3", "4"]:
        print("\nOpción no válida. Por favor, elija una opción del 1 al 5.")
        continue

    try:
        numero1 = float(input("\nIngrese el primer número: "))
        numero2 = float(input("\nIngrese el segundo número: "))
    except ValueError:
        print("¡Error! Por favor, ingrese números válidos.")
        continue
    if opcion == "1":
        resultado = suma(numero1, numero2)
        print(f"\nEl resultado de la suma es: {resultado}")
    elif opcion == "2":
        resultado = resta(numero1, numero2)
        print(f"\nEl resultado de la resta es: {resultado}")
    elif opcion == "3":
        resultado = multiplicacion(numero1, numero2)
        print(f"\nEl resultado de la multiplicación es: {resultado}")
    elif opcion == "4":
        try:
            resultado = division(numero1, numero2)
            print(f"\nEl resultado de la división es: {resultado}")
        except ZeroDivisionError:
            print("\nError! No se puede dividir por cero.")
 
    print()  # Añadir una línea en blanco para mejorar la legibilidad
    print("\nOperación completada. Puede realizar otra operación o salir.")

    print()  # Añadir una línea en blanco para mejorar la legibilidad
    

# Fin del código

