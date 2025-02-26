# Encuentra el animal con más letras de la lista

matriz = [
    ["Perro", "Gato", "Hámster"],
    ["Loro", "Conejo", "Tortuga"],
    ["Pez", "Hurón", "Ardilla"],
    ["Iguana", "Serpiente", "Erizo"]
]

palabra_grande = matriz[0][0]

for fila in matriz:
    for animal in fila:
        if len(animal) > len(palabra_grande):
            palabra_grande = animal

print(f"La palabra con más letras de la matriz es: {palabra_grande}")