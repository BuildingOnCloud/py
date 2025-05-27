#to-do-list
#  Gestión de Tareas:
# Cree un programa simple para gestionar tareas pendientes. 
# El programa permitirá al usuario agregar tareas, ver la lista de tareas pendientes, marcar tareas como completadas y eliminar tareas. 
# Utilize listas para almacenar las tareas.


toDoList[]



# Ciclamos mientras mientras el usuario no eliga Salir
while True:
    print("\nGestión de Tareas")
    print("1. Agregar Tarea")
    print("2. Ver Tareas Pendientes")
    print("3. Marcar Tarea como Completada")
    print("4. Eliminar Tarea")
    print("5. Salir")

    opcion = input("Selecciona una opción (1/2/3/4/5): ")

    elif opcion == "5": # Salir

        print("¡Hasta luego!")
    break

    else:   # Opcion de Menu No Valida

        print("Opción no válida. Por favor, selecciona una opción válida.")
