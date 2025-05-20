print ("Calculadora Basica by Python")
numero_1 = float(input("Ingrese un numero:"))
numero_2 = float(input("Ingreso otro numero:"))

Opcion = 0

while Opcion != 5:
    print("""
    Selecciona una opcion:
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir
          
 """)
    
    Opcion = int(input())

    if Opcion == 1:
        print(" ")
        print("Resultado:", numero_1,"+",numero_2,"=",numero_1 + numero_2)
    if Opcion == 2:
        print(" ")
        print("Resultado:", numero_1,"-",numero_2,"=",numero_1 - numero_2)
    if Opcion == 3:
        print(" ")
        print("Resultado:", numero_1,"*",numero_2,"=",numero_1 * numero_2)
    if Opcion == 4:
        if numero_2 != 0:
            print(" ")
            print("Resultado:",numero_1,"/",numero_2,"=",numero_1 / numero_2)
        else:
            print("No se puede dividir entre cero")
    if Opcion == 5:
        print(Gracias por usal la Calculadora CloudLamp elearning)
input()
