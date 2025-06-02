def registrar_temperaturas():
    temperaturas = {}  # Diccionario para almacenar fecha: temperatura
    while True:
        fecha = input("Ingresa la fecha (YYYY-MM-DD) o 'salir' para terminar: ")
        if fecha.lower() == 'salir':
            break
        if fecha in temperaturas:
            print("La fecha ya ha sido registrada. Por favor, ingresa una fecha diferente.")
            continue
        try:
            temp = float(input("Ingresa la temperatura para esa fecha: "))
            temperaturas[fecha] = temp
        except ValueError:
            print("Por favor, ingresa una temperatura válida.")
    return temperaturas

def calcular_estadisticas(temperaturas):
    if not temperaturas:
        print("No hay datos para calcular estadísticas.")
        return None
    temps = list(temperaturas.values())
    promedio = sum(temps) / len(temps)
    max_temp = max(temps)
    min_temp = min(temps)
    # Guardamos los resultados en una tupla
    estadisticas = (promedio, max_temp, min_temp)
    return estadisticas

def main():
    temperaturas = registrar_temperaturas()
    estadisticas = calcular_estadisticas(temperaturas)
    if estadisticas:
        promedio, max_temp, min_temp = estadisticas
        print(f"\nEstadísticas registradas:")
        print(f"Promedio de temperaturas: {promedio:.2f}")
        print(f"Temperatura máxima: {max_temp}")
        print(f"Temperatura mínima: {min_temp}")
        print()


        
if __name__ == "__main__":
    main()