# Encuentra el número de animales que empiezan por vocal

matriz = [
    ["Perro", "Gato", "Hámster"],
    ["Loro", "Conejo", "Tortuga"],
    ["Pez", "Hurón", "Ardilla"],
    ["Iguana", "Serpiente", "Erizo"]
]

vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
contador = 0
for fila in matriz:
    for animal in fila:
        if animal[0] in vocales:
            contador+=1
print(f"Los animales que empiezan por vocales son: {contador}")
