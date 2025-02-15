import random

def lanzar_moneda():
    if random.randint(0, 1) == 0:
        return "Cara"
    return "Cruz"

def lanzar_dado():
    return random.randint(1, 6)

def elegir_numero_loteria():
    numero = random.randint(0, 99999)
    return numero

def generar_contraseña(longitud=8):
    contraseña = ""
    for i in range(longitud):
        letra = random.choice("abcdefghijklmnopqrstuvwxyz")
        contraseña += letra
    return contraseña

def seleccionar_elemento(lista):
    if lista:
        indice = random.randint(0, len(lista) - 1)
        elemento = lista[indice]
        return elemento
    return None