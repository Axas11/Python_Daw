import random
def generarCarta() -> str:

    paloCodigo = random.randint(1, 4)

    if paloCodigo == 1:
        palo = "picas"
    elif paloCodigo == 2:
        palo = "diamantes"
    elif paloCodigo == 3:
        palo = "treboles"
    elif paloCodigo == 4:
        palo = "corazones"
    
    numero = str(random.randint(1, 13))

    if numero == "11":
        numero = "J"
    elif numero == "12":
        numero = "Q"
    elif numero == "13":
        numero = "K"
    
    carta = numero + " de " + palo

    return carta
i = 0
CartaElegida = input("Elige una carta (7 de picas): ")
contador = 0
tirada1 = 0
while True:
    cartaSacada = generarCarta()
    print(f"Tirada {i}: {cartaSacada}")
    if CartaElegida == cartaSacada:
        contador = contador + 1
     
    if contador == 2:
        break

    i += 1

print(f"La primera carta se ha encontrado en X intentos y la segunda en {i} intentos")    
