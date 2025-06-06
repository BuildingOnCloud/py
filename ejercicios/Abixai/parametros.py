#Modulo para calcular operaciones matematicas basicas

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        
        return "Dígito no válido"
    return a / b