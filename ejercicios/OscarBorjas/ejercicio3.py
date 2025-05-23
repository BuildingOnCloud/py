print("**Calculadora**")
print("Ingrese el tipo de operacion a realizar")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

operac = input()

numeroA = input("Ingrese el primer numero: ")
numeroB = input("Ingrese el segundo numero: ")


if numeroA.isdigit() and numeroB.isdigit():
    numeroA =  float(numeroA)
    numeroB =  float(numeroB)
#    print(type(numeroA))
#    print(type(numeroB))
#if type(numeroA) == float and type(numeroB) == float:
    if operac == "1":
        print("Suma")
        resultado = numeroA + numeroB
        print("El resultado es: "+ str(resultado))
    elif operac == "2":
        print("Resta")
    
        resultado = numeroA - numeroB
        print("El resultado es: "+ str(resultado))
    elif operac == "3":
        print("Multiplicacion")
        resultado = numeroA * numeroB
        print("El resultado es: "+ str(resultado))
    elif operac == "4":
        print("Division")
        if numeroB == 0:
            print("Error division por 0")
        else:
            resultado = numeroA / numeroB
            print(f"El resultado es: {resultado}")
    else:
        print("Opcion equivocada")
else:
    print("ha colocado datos invalidos repita el procedimieno")
