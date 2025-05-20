#https://github.com/BuildingOnCloud/py.git
#
#----------------------------
#Ejercicio Calculadora
#Tarea: agregar validaciones al input

Numero_1 = float (0.0)
Numero_2 = float (0.0)
Resultado = float (0.0)

menu = int (0)

Numero_1 = float(input("Hola, por favor introduce tu primera cifra. "))
Numero_2 = float(input("Por favor introduce tu segunda cifra. "))

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
		print("division por 0 no es valida, introduzca de nuevo. ")
	else:
		Resultado = Numero_1 / Numero_2
		print(f"Su resultado es {Resultado}" )	#Convierte Resultado en str
		
else: print("Opcion no valida")
