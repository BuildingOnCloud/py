#to-do-list
#  Gestión de Tareas:
# Cree un programa simple para gestionar tareas pendientes. 
# El programa permitirá al usuario agregar tareas, ver la lista de tareas pendientes, marcar tareas como completadas y eliminar tareas. 
# Utilize listas para almacenar las tareas.


toDolist=[]
# Ciclamos mientras mientras el usuario no eliga Salir
while True:
    print("\nGestión de Tareas")
    print("1. Agregar Tarea")
    print("2. Ver Tareas Pendientes")
    print("3. Marcar Tarea como Completada")
    print("4. Eliminar Tarea")
    print("5. Salir")

    opcion = int(input("Selecciona una opción (1/2/3/4/5): ")) #Agregar validacion para string 

    if opcion == 1:   
        toDolist.append(input("Escriba el nombre de la tarea: "))

    elif opcion == 2:
        if len(toDolist)>0:     #Colocar esta validacion donde se requiera imprimir la lista
            print("Tareas pendientes:")
            #print(toDolist)
            index = 1
            for tarea in toDolist:
                print(str(index) +" "+tarea)
                index += 1
        else:
            print("Lista de tareas Vacia")
    elif opcion == 3:           #Validar que el indice ingresado exista dentro de la lista, ademas validar contra alfanumerico
        index = 1
        for tarea in toDolist:
            print(str(index) +" "+tarea)
            index += 1
        tareaEliminar = input(" Ingrese el indice de la tarea a completar: ")
        toDolist.pop(int(tareaEliminar)-1)
        
        #del toDolist[index-1]
        #toDolist.remove(index-1)
    elif opcion == 4:           #Validar que el indice ingresado exista dentro de la lista, ademas validar contra alfanumerico
        index = 1
        for tarea in toDolist:
            print(str(index) +" "+tarea)
            index += 1
        tareaEliminar = input(" Ingrese el indice de la tarea a Eliminar: ")
        toDolist.pop(int(tareaEliminar)-1)
    elif opcion == 5: # Salir

        print("¡Hasta luego!")
        break

    else:   # Opcion de Menu No Valida

        print("Opción no válida. Por favor, selecciona una opción válida.")