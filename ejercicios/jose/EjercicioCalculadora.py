#https://github.com/BuildingOnCloud/py.git
#
#----------------------------
#Ejercicio Calculadora
#Tarea: agregar validaciones al input

Numero_1 = float (0.0)
Numero_2 = float (0.0)
Resultado = float (0.0)
menu = str (0)


print("¡Bienvenido a la Calculadora de Jose Manuel! ")

while True:
    try:
        Numero_1 = float(input("Por favor introduce tu primera cifra. "))
        break  # Si la conversión fue exitosa, salimos del bucle
    except ValueError:
        print("¡Error! Eso no es una cifra válida. Por favor, introduce un número.")

while True:
    try:
        Numero_2 = float(input("Por favor introduce tu segunda cifra. "))
        break  # Si la conversión fue exitosa, salimos del bucle
    except ValueError:
        print("¡Error! Eso no es una cifra válida. Por favor, introduce un número.")

        

print("1. Suma (+)")
print("2. Resta (-)")
print("3. Multiplicación (*)")
print("4. División (/)")

menu = input("Seleccion la operacion que desea realizar: ")

if menu == "1":
	Resultado = Numero_1 + Numero_2
	print(f"Su resultado es {Resultado}" )	#Convierte Resultado en str
elif menu == "2":
	Resultado = Numero_1 - Numero_2
	print(f"Su resultado es {Resultado}" )	#Convierte Resultado en str
elif menu == "3":
	Resultado = Numero_1 * Numero_2
	print(f"Su resultado es {Resultado}" )	#Convierte Resultado en str
elif menu == "4":
	if Numero_2 == 0:
		print("division por 0 no es valida. ")
	else:
		Resultado = Numero_1 / Numero_2
		print(f"Su resultado es {Resultado}" )	#Convierte Resultado en str
		
else: print("Opcion no valida")