
# 1. Definimos el "Molde" o "Clase" para nuestros vehiculos
#    (Vehiculo es la clase base, Coche y Bicicleta son clases derivadas)
class Vehiculo:
    # 2. El constructor: se ejecuta cuando creamos un nuevo vehiculo
    #    (marca, modelo, color, velocidad, nro_ruedas son atributos comunes)
    def __init__(self,marca, modelo, color, velocidad, nro_ruedas):
        # 3. Atributos: características de cada vehiculo
        #    (marca, modelo, color, velocidad, nro_ruedas son atributos de Vehiculo)
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad
        self.nro_ruedas = nro_ruedas
    # 4. Métodos: acciones que puede hacer un vehiculo  
    #    (acelerar, frenar, arrancar, apagar son acciones comunes)
    #    (en este caso, los métodos están definidos pero no implementados)  
    def acelerar(self):
        pass
    def frenar(self):
        pass
    def arrancar(self):
        pass
    def apagar(self):
        pass

class Coche(Vehiculo):
    def __init__(self,marca, modelo, color, velocidad, nro_ruedas,tipo_motor, combustible,traccion):
        super().__init__(marca,modelo,color,velocidad,nro_ruedas)
        self.tipo_motor = tipo_motor
        self.combustible = combustible
        self.traccion = traccion
    def arrancar(self):
        print(f"El {self.marca} {self.modelo} {self.color} ha arrancado.")

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color, velocidad, nro_ruedas,tamano_rin,tipo,tipo_traccion,velocidad_actual):
        super().__init__(marca, modelo, color, velocidad, nro_ruedas)
        self.tamano_rin = tamano_rin
        self.tipo = tipo
        self.tipo_traccion = tipo_traccion
        self.velocidad_actual = velocidad_actual
    def subir_velocidad(self):
        self.velocidad_actual += 1
    def bajar_velocidad(self):
        self.velocidad_actual -= 1

# --- Ahora creamos nuestros "Objetos" o "Instancias" de la Clase Vehiculo ---

#  Creamos el primer vehiculo: un coche Toyota rojo
mi_coche_rojo = Coche("Toyota","Yaris", "rojo", "4 Ruedas", "1.5L", "Gasolina", "Delantera")

#  Creamos el segundo vehiculo: una bicicleta OxFord azul
mi_bicicleta_azul = Bicicleta("OxFord", "azul", "Aluminio", "Montaña", "Delantera", 21) 