#  Calculadora de Operaciones Básicas
#  Crea un programa en Python que permita al usuario realizar operaciones básicas de suma, resta, multiplicación y división.
#  El programa debe solicitar al usuario que ingrese dos números y luego seleccionar la operación que desea realizar. Después,
#  debe mostrar el resultado de la operación.
# Nota: Use la operacion input() para leer el ingreso de información. 


# Primero declaro el tipo de datos
Numero1 = float (0.0)
Numero2 = float (0.0)
Resultado = float (0.0)
Opcion = int (0)

# Luego ingreso funcion de entrada de datos dentro de la variable
def calculadora ():
    try:
        Numero1 = float(input("Ingrese el primer numero: "))
        Numero2 = float(input("Ingrese el segundo numero: "))
        """esta funcion intenta convertir 
        la cadena de texto ingresada
        por el usuario a un numero 
        de punto flotante (un numero decimal).
        El resultado se almacena en la variable. """
    except ValueError:
        print("¡Error! Por favor, ingrese números válidos.")
        return

#Imprimo las funciones de la calculadora

    print("Elija una opcion: ")
    print("1. Suma (+) ")
    print("2. Resta (-) ")
    print("3. Multiplicacion (*) ")
    print("4. Division (/)")

    Opcion = input("Selecione la operacion a realizar: ")

    if Opcion == "1":
        Resultado = Numero1 + Numero2
        print(f"Su resultado es: {Resultado} ")
        """la f antes de una cadena de texto en
        Python la convierte en un f-string,
        lo que te permite incrustar expresiones
        de Python (como el valor de una variable)
        directamente dentro de la cadena utilizando llaves {}"""
    elif Opcion == "2":
        Resultado = Numero1 - Numero2
        print(f"Su resultado es: {Resultado} ")
    elif Opcion == "3":
        Resultado = Numero1 * Numero2
        print(f"Su resultado es: {Resultado} ")
    elif Opcion == "4":
        if Numero2 == 0:
            print("division por 0 no es valida, introduzca de nuevo. ")       
        else: 
            Resultado = Numero1 / Numero2
            print(f"Su resultado es: {Resultado} ")
    else:
        print("Opcion invalida Por favor, seleccione una opcion del 1 al 4.")
if __name__ == "__main__":
    calculadora()









                  


