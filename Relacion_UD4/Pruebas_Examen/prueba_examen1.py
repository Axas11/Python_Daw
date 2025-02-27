# 1. Listas (1 punto) - Animales
animales = ["Perro", "Gato", "Pájaro"]
for animal in animales:
    print(animal)

# 2. Listas (1 punto) - Animales
animales.append("Conejo")
print(animales)

# 3. Listas (2 puntos) - Fútbol
equipos = ["Chipiona", "Madrid", "Barcelona", "Betis", "Sevilla"]
equipos[2] = "Cádiz"
print(equipos)

# 4. Listas (1 punto) - Sin temática (Borja Panoli)
borja = ["Borja", "Panoli", "Campeón"]
borja.pop()
print(borja)

# 5. Listas (2 puntos) - Notas Musicales
notas = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"]
notas.remove("Fa")
notas.append("Fa#")
print(notas)

# 6. Matrices (Regalado)
matriz = [[1, 2], [3, 4]]
for fila in matriz:
    print(fila)

# 7. Matrices (Planetas - Más complicado)
planetas = [["Mercurio", "Venus", "Tierra"], ["Marte", "Júpiter", "Saturno"], ["Urano", "Neptuno", "Plutón"]]
planetas[0], planetas[2] = planetas[2], planetas[0]
for fila in planetas:
    print(fila)