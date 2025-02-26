import random
# Dada una lista con 2^n elementos, por ejemplo:
# Crear una función que imprima por pantalla el emparejamiento aleatorio de todos los elementos de la lista
tenistas_top_8 = [
    "Jannik Sinner","Alexander Zverev","Carlos Alcaraz","Taylor Fritz",       
    "Casper Ruud","Daniil Medvedev","Novak Djokovic","Álex de Miñaur"      
]

def mostrar_enfrentamientos(tenistas_top_8:list):
    tenistas = tenistas_top_8.copy()
    print("Enfrentamientos:")
    while tenistas:
        pos_1 = random.randint(0,len(tenistas)-1)
        jugador1 = tenistas.pop(pos_1)

        pos_2 = random.randint(0,len(tenistas)-1)
        jugador2 = tenistas.pop(pos_2)
        print(f"{jugador1} vs {jugador2}")

mostrar_enfrentamientos(tenistas_top_8)