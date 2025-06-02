# to-do-list
tareas = []

def mostrar_menu():
    print("\nGestor de Tareas")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def agregar_tarea():
    tarea = input("Ingresa la tarea: ")
    tareas.append({"descripcion": tarea, "completada": False})
    print(f"Tarea '{tarea}' agregada.")

def ver_tareas():
    if not tareas:
        print("No hay tareas pendientes.")
        return
    print("\nLista de tareas:")
    for idx, tarea in enumerate(tareas, 1):
        estado = "✔️" if tarea["completada"] else "❌"
        print(f"{idx}. {tarea['descripcion']} [{estado}]")

def marcar_completada():
    ver_tareas()
    if not tareas:
        return
    try:
        num = int(input("Ingresa el número de la tarea a marcar como completada: "))
        if 1 <= num <= len(tareas):
            tareas[num - 1]["completada"] = True
            print(f"Tarea '{tareas[num - 1]['descripcion']}' marcada como completada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def eliminar_tarea():
    ver_tareas()
    if not tareas:
        return
    try:
        num = int(input("Ingresa el número de la tarea a eliminar: "))
        if 1 <= num <= len(tareas):
            tarea_eliminada = tareas.pop(num - 1)
            print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            agregar_tarea()
        elif opcion == '2':
            ver_tareas()
        elif opcion == '3':
            marcar_completada()
        elif opcion == '4':
            eliminar_tarea()
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()