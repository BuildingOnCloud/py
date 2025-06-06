from parametros import suma, resta, multiplicacion, division

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
        print(f"\nEl resultado es: {resultado}")
    elif opcion == "2":
        resultado = resta(numero1, numero2)
        print(f"\nEl resultado es: {resultado}")
    elif opcion == "3":
        resultado = multiplicacion(numero1, numero2)
        print(f"\nEl resultado es: {resultado}")
    elif opcion == "4":
        try:
            resultado = division(numero1, numero2)
            print(f"\nEl resultado es: {resultado}")
        except ZeroDivisionError:
            print("\No se puede dividir por cero.")
 
    print()  
    print("\nOperación completada. Puede realizar otra operación o salir.")

    print() 
    
