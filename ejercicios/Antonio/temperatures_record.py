#Función para calcular el promedio de temperaturas
print("""
      Temperatures Records
      ********************""")
def calc_average(temps):
    if len(temps) == 0:
        return 0
    addition = sum(temps)
    average = addition / len(temps)
    return average

# Función para encontrar la temperatura máxima
def find_max(temps):
    return max(temps)

# Función para encontrar la temperatura mínima
def find_min(temps):
    return min(temps)

# Programa principal
record_temps = {}  # Usamos un diccionario para registrar temperaturas con fechas

while True:
    date = input("Input date (or 'end' to fihish): ")
    
    if date.lower() == "end":
        break
    
    try:
        temp = int(input("input a temp: "))
        
        if date in record_temps:
            record_temps[date].append(temp)
        else:
            record_temps[date] = [temp]
    except ValueError:
        print("Input invalid. Input date and Temp válid or 'end' to finish.")

if not record_temps:
    print("No input temps.")
else:
    for date, temps in record_temps.items():
        average = calc_average(temps)
        maxi = find_max(temps)
        mini = find_min(temps)
        
        print(f"Date: {date}")
        print(f"Temperature: {temps}")
        print(f"Temp Average: {average:.2f}")
        print(f"Temp Max: {maxi}")
        print(f"Temp Min: {mini}")
        print()

# Conversión del registro de temperaturas en un diccionario inmutable (tupla de tuplas)
registro_temperaturas = tuple((date, tuple(temps)) for date, temps in record_temps.items())

print(f"Record Temps en una Tupla de Tuplas:\n{registro_temperaturas}")