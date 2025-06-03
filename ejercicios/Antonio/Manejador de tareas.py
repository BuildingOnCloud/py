Python 3.14.0b1 (tags/v3.14.0b1:b092705, May  7 2025, 10:22:31) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print (""" 
          _______________
          Manejador de Tareas
          ***************        
       """)
pending = []
while True:
...     print("""
...     1. Agregar Tarea
...            
...     2. Ver lista de Tareas
...           
...     3. Cambiar estado a hecho
...           
...     4. Eliminar Tarea
...           
...     5. Salir
...     """)
...     option = input("Selecciona una opcion:")
...     if option == "5":
...        print("""
...              **** Gracias por usar el manejador de tareas ****
...              """)
...        break
...     
...    
...     elif option == "1":
...         print("Option 1 selected")
...         print()
...         task = input("Input a task to do:")
...         pending.append(task)
...     
...     elif option == "2":
...         print("Option 2 Selected")
...         print("Tasks list")
...         for i, task in enumerate(pending, 1):
...             print(f"{i}.{task}")
...    
...     elif option == "3":
...         print("Option 3 selected")
...         for i, task in enumerate(pending, 1):
...             print(f"{i}. {task}")
...         done = int(input ("Select a number of task done:"))
...         if 1<= done <=len(pending):
...             task_done = pending [done -1]
...             del pending [done-1]
...             print(f"The task changed to done: {task_done}")
        else:
            print("""
                      ***Task not found***
                  """)

    elif option == "4":
        print("Option 4 Selected")
        for i, task in enumerate(pending, 1):
            print(f"{i}. {task}")
        delete = int(input ("Select a number of task to delete:"))
        if 1<= delete <=len(pending):
            task_delete = pending [delete -1]
            del pending [delete-1]
            print(f"The task was deleted: {task_delete}")
    else:
        print("""
               ******   Invalid  ********
                Select a correct option
               **************************
