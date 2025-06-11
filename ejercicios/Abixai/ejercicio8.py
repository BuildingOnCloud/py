class Vehiculo:
    def __init__(self,marca, modelo, color, velocidad, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad
        self.nro_ruedas = nro_ruedas
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

mi_coche_rojo = Coche("Toyota","Yaris", "rojo", "4 Ruedas", "1.5L", "Gasolina", "Delantera")

mi_bicicleta_azul = Bicicleta("OxFord", "azul", "Aluminio", "Montaña", "Delantera", 21) 