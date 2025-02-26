# Muestra la posición y valor de cada elemento en la lista
frutas = ["manzana", "pera", "naranja"]
for indice, fruta in enumerate(frutas, 1):
    print(f"{indice}. {fruta.capitalize()}")