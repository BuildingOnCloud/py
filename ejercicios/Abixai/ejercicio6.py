Registro_de_temperaturas = {}

def Registrar_temperaturas ():

    while True:

        try:
            fecha = input ("\nPor favor, ingresar la fecha, ejemplo: AAAA-MM-DD (de lo contrario escribe 'fin' para regresar): ")
        
            if fecha.lower() == "fin":
                break

            temperaturas = float(input("Por favor ingresar una temperatura: "))
            Registro_de_temperaturas[fecha]= temperaturas        

        except ValueError:
            print("\nEntrada no valida, por favor ingresar una fecha y temperatura valida (de lo contrario escribe 'fin' para terminar): ") 

def mostrar_temperaturas ():

    if len(Registro_de_temperaturas) == 0:
        print("\nNo hay fechas ni temperaturas registradas aun, elija la opcion: 1. ")
    else:
        for fecha, temperaturas in Registro_de_temperaturas.items():
            print(f"\nFecha: {fecha} | Temperatura: {temperaturas}°C")


def calcular_estadisticas ():
     
     if len(Registro_de_temperaturas) == 0:
        print("\nNo hay fechas ni temperaturas registradas aun para el calculo de estadisticas, elija la opcion: 1. ")        
     else:
        lista_temperaturas = list (Registro_de_temperaturas.values())
        suma = sum(lista_temperaturas)
        promedio= suma / len(lista_temperaturas)
        promedio_red= round(promedio, 2)
        maxima = max(lista_temperaturas)
        maxima_red= round(maxima, 1)
        minima = min(lista_temperaturas)
        minima_red= round(minima, 1)
        estadisticas_calculadas = (promedio, maxima, minima)
        print(f"\nPromedio: {promedio_red}°C | Maxima: {maxima_red}°C |  Minima {minima_red}°C")
        return estadisticas_calculadas
     
while True:

    print("\nMenu de Opciones:")
    print("1. Registrar temmperaturas")
    print("2. Mostrar temperaturas guardadas")
    print("3. Estadisticas de temperaturas")
    print("4. Salir")


    try:
        opcion = int (input("\nPor favor elija una opcion para ejecutar: "))

        if opcion == 1:
           Registrar_temperaturas ()


        elif opcion == 2:
            mostrar_temperaturas ()
        
        elif opcion == 3:
            calcular_estadisticas ()

        elif opcion == 4:
            print("Hasta Luego.")
            break

        else: 

            print("\nOpción no válida. Por favor, elija un numero dentro del menu.")

    except ValueError:
            print("\nEntrada no valida, Intentar de nuevo. ")

