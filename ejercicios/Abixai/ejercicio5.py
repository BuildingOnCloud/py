toDolist=[]

while True:
    print("\nGestión de Tareas")
    print("1. Agregar Tarea")
    print("2. Ver Tareas Pendientes")
    print("3. Marcar Tarea como Completada")
    print("4. Eliminar Tarea")
    print("5. Salir")

    opcion = int(input("Selecciona una opción (1/2/3/4/5): ")) 

    if opcion == 1:   
        toDolist.append(input("Escriba el nombre de la tarea: "))

    elif opcion == 2:
        if len(toDolist)>0:     
            print("Tareas pendientes:")
            index = 1
            for tarea in toDolist:
                print(str(index) +" "+tarea)
                index += 1
        else:
            print("Lista de tareas Vacia")
    elif opcion == 3:        
        index = 1
        for tarea in toDolist:
            print(str(index) +" "+tarea)
            index += 1
        tareaEliminar = input(" Ingrese el indice de la tarea a completar: ")
        toDolist.pop(int(tareaEliminar)-1)
        
    elif opcion == 4:   
        index = 1
        for tarea in toDolist:
            print(str(index) +" "+tarea)
            index += 1
        tareaEliminar = input(" Ingrese el indice de la tarea a Eliminar: ")
        toDolist.pop(int(tareaEliminar)-1)
    elif opcion == 5: 

        print("¡Hasta luego!")
        break

    else:  

        print("Opción no válida. Por favor, selecciona una opción válida.")