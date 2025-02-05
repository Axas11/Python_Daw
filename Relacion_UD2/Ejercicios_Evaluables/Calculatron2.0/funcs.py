import random

def menu():
    print("CALCULATRON 2.0")
    print("1. Jugar")
    print("2. Configuracion")
    print("3. Estadisticas")
    print("4. Logros")
    print("0. Salir")

def cuentaRandom(numMin, numMax):
    operador1 = random.randint(numMin, numMax)
    operador2 = random.randint(numMin, numMax)
    operador = random.choice(["+", "-", "*"])
    
    if operador == "+":
        resultado = operador1 + operador2
    elif operador == "-":
        resultado = operador1 - operador2
    else:
        resultado = operador1 * operador2
    
    print(f"{operador1} {operador} {operador2} = ?")
    return resultado

def estadisticas(numJugadas, operacionTotal, aciertosTotales, fallosTotal, rachaMax):
    print(f"Jugado:  {numJugadas} partidas")
    print(f"Total:  {operacionTotal} operaciones")
    print(f"Aciertos: {aciertosTotales} operaciones")
    
    if operacionTotal == 0:
        print("Porcentaje de aciertos: 0%")
    else:
        print(f"Porcentaje de aciertos: {round(aciertosTotales * 100 / operacionTotal, 2)}% ")
        print(f"Fallos: {fallosTotal} operaciones")
    
    if operacionTotal == 0:
        print("Fallos: 0%")
    else:
        print(f"Fallos: {round(fallosTotal * 100 / operacionTotal, 2)}% ")
    
    print(f"RachaMax: {rachaMax} aciertos")

def configuracion(vidasConf, numMin, numMax):
    print("Configuracion actual:")
    print(f"Vidas: {vidasConf}")
    print(f"NumMin: {numMin}")
    print(f"NumMax: {numMax}")
    print("1. Cambiar numero de vidas")
    print("2. Cambiar numMin")
    print("3. Cambiar numMax")
    print("0.salir")

def logros(bronce, plata, oro, platino):
    if bronce:
        print("Bronce: Conseguido")
    else:
        print("Bronce: No conseguido")
    
    if plata:
        print("Plata: Conseguido")
    else:
        print("Plata: No conseguido")
    
    if oro:
        print("Oro: Conseguido")
    else:
        print("Oro: No conseguido")
    
    if platino:
        print("Platino: Conseguido")
    else:
        print("Platino: No conseguido")
    