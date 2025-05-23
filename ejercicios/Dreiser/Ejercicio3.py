print("Menu de calculadora")
print("Selecciona la operacion a realizar")
print("1. Suma (+)")
print("2. Resta ()")
print("3. Multiplicación (*)")
print("4. División (/)")

opcion = input("Ingresa el número de la operación (1-4): ")

num1 = float(input("Ingrese el número 1: "))
num2 = float(input("ingrese el número 2: "))
if numeroA.isdigit() and numeroB.isdigit():
    num1 =  float(numeroA)
    num2 =  float(numeroB)

    if opcion == "1":
	
    	num1 = float(input("Ingrese el número 1: "))
    	num2 = float(input("ingrese el número 2: "))
    	total = num1 + num2
    	print(f"El resultado de la suma es: {total}")
    elif opcion == "2":
    	num1 = float(input("Ingrese el número 1: "))
    	num2 = float(input("ingrese el número 2: "))
    	total = num1 - num2
    	print(f"El resultado de la resta es: {total}")
    elif opcion == "3":
    	num1 = float(input("Ingrese el número 1: "))
    	num2 = float(input("ingrese el número 2: "))
    	total = num1 * num2
    	print(f"El resultado de la multiplicación es: {total}")
    elif opcion == "4":
    	num1 = float(input("Ingrese el número 1: "))
    	num2 = float(input("ingrese el número 2: "))
    	if num2 != 0:
           total = num1 / num2
           print(f"El resultado de la división es: {total}")
   	else:
           print("error, no se puede dividir entre cero (0)")
    else:
    	print("No es una opción valida selecciona entre 1 y 4")
else:
    print("ha colocado datos invalidos repita el procedimieno")