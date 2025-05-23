valor1 = float (0.0)
valor2 = float (0.0)
operacion = int (0)
resultado = float (0.0)


print("Cifra 1:")
valor1 = float(input("ingresa tu primera cifra "))
print("Cifra 2:")
valor2 = float(input("ingresa tu segunda cifra "))

if valor1 or valor2 == "" :
            print("This cannot be blank. Please re-enter.")

elif valor1.isdigit() == False:
            print("Must be numbers only. Please re-enter.")

elif valor2.isdigit() == False:
            print("Must be numbers only. Please re-enter.")



print("Selecciona la operación a realizar")

print("1. Suma (+)")
print("2. Resta (-)")
print("3. Multiplicación (*)")
print("4. División (/)")

operacion = input("Mi operación es: ")


if operacion == "" :
            print("This cannot be blank. Please re-enter.")

elif operacion  == "1" :

    resultado = valor1+valor2
    print(f"Su resultado es: {resultado}")

elif  operacion  == "2" :

    resultado = valor1-valor2
    print(f"Su resultado es: {resultado}")

elif  operacion  == "3" :

    resultado = valor1*valor2
    print(f"Su resultado es: {resultado}")

elif  operacion  == "4" :

    resultado = valor1/valor2
    print(f"Su resultado es: {resultado}")

else :
    print("Operación no válida")