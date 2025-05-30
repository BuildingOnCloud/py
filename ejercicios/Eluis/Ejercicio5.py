#Gestión de Tareas
#Cree un programa simple para gestionar tareas pendientes. 
#El programa permitirá al usuario agregar tareas, ver la lista de tareas pendientes, marcar tareas como completadas y eliminar tareas.
#Utilize listas para almacenar las tareas.

lista_tareas_principal= []
# Ciclamos mientras mientras el usuario no eliga Salir
while True:
    print("\nGestión de Tareas")
    print("1. Agregar Tarea")
    print("2. Ver Tareas Pendientes")
    print("3. Marcar Tarea como Completada")
    print("4. Eliminar Tarea")
    print("5. Salir")
    

    opcion = input("\nSelecciona una opción (1/2/3/4/5): ") #Agregar validacion para string
    

    if opcion == "1":
        lista_tareas_principal.append(input("\nEscriba el nombre de la Tarea: ")) #Admite/almacena a la "lista_tareas_principal" una nueva tarea con su nombre en el ultimo lugar de la lista en tipo caracter str

    elif opcion == "2":
        if len(lista_tareas_principal)>0: #Si es mayor a 0 continua la sentencia FOR
            print("tareas pendientes: ") 
            #iteramos con FOR en cada elemneto almacenado en "lista_tareas_principal" y vamos mostrando todo lo que contiene
            index = 1  #esta variable representa la enumeracion de cada tarea      
            for tarea in lista_tareas_principal: #itera con nueva variable "tarea" con el valor de cada indice dentro de la lista de "lista_tareas_principal"
                print(str(index) + " " + tarea) #imprime convirtiendo como caracter el valor de "index" adicionando como cadena de caracer el valor de "tarea"
                index += 1 # este operador me suma al valor actual de "index" el numero 1, en este caso seria =2, y vuelve el ciclo de iteracion hasta terminar la sentencia for
        else:
            print("Usted aun no ha ingresado traeas a su lista, por favor ingresar su primera tarea. ") # de no cumplirse la condicion de la opcion 2

    elif opcion == "3":
        if len(lista_tareas_principal)>0:
            index = 1
            for tarea in lista_tareas_principal:
                print(str(index) + " " +tarea)
                index += 1
            Eliminar_tarea = input("\nIngrese el numero de la tarea a marcar como completada: ")
            lista_tareas_principal.pop(int(Eliminar_tarea)-1)    #.pop(): Este es un método que elimina y devuelve un elemento de una lista en un índice (posición) específico
        else:
            print("Usted aun no ha ingresado traeas a su lista, por favor ingresar su primera tarea. ")                                                            # entonces me elimina la posicion del indice del numero ingresado restandole -1 para que de el numero de indice correcto

    elif opcion == "4":
        if len(lista_tareas_principal)>0:
            index = 1
            for tarea in lista_tareas_principal:
                print(str(index) + "" +tarea)
                index += 1
            Eliminar_tarea_str = input("\nIngrese el numero de la tarea que desea eliminar: ")
            if Eliminar_tarea_str.isdigit():  # Verificar si la entrada es un número
                Eliminar_tarea = int(Eliminar_tarea_str)
                if 1 <= Eliminar_tarea <= len(lista_tareas_principal):
                    lista_tareas_principal.pop(Eliminar_tarea - 1)
                else:
                    print("Número de tarea inválido. Por favor, ingrese un número de la lista.")
            else:
                print("Entrada inválida. Por favor, ingrese un número.")   
        else:
            print("Usted aun no ha ingresado traeas a su lista, por favor ingresar su primera tarea. ")  
        
              


    elif opcion == "5": # Salir

        print("¡Hasta luego!")
        break
    

    else:   # Opcion de Menu No Valida

        print("Opción no válida. Por favor, selecciona una opción válida.")

