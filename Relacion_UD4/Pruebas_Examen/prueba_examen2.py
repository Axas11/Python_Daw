# 1. Listas - Animales (más complejo)
animales = ["Perro", "Gato", "Pájaro"]
animales_mod = [animal.upper() + " (" + str(animales.index(animal)) + ")" for animal in animales]
animales_mod.insert(1, "LEÓN")
for i in range(len(animales_mod)):
    print(f"Animal en posición {i}: {animales_mod[i]}")

# 2. Listas - Animales (más complejo)
animales = ["Perro", "Gato", "Pájaro"]
animales.extend("Conejo León Tigre".split())
contador = len([x for x in animales if len(x) > 4])
print(f"Lista extendida: {animales}")
print(f"Animales con más de 4 letras: {contador}")

# 3. Listas - Fútbol (más complejo)
equipos = ["Chipiona", "Madrid", "Barcelona", "Betis", "Sevilla"]
equipos[1:3] = ["Cádiz", "Atlético"]
equipos.sort(reverse=True)
if len(equipos[-1]) > 6:
    equipos.pop()
print(f"Equipos modificados y ordenados: {equipos}")

# 4. Listas - Sin temática (Borja Panoli) (más complejo)
borja = ["Borja", "Panoli", "Campeón"]
borja_copia = borja.copy()
elemento = borja_copia.pop(1)
borja_copia.insert(0, elemento + " 2.0")
print(f"Lista original: {borja}")
print(f"Lista modificada: {borja_copia}")

# 5. Listas - Notas Musicales (más complejo)
notas = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"]
indice_fa = notas.index("Fa")
notas[indice_fa:indice_fa+1] = ["Fa#", "Fa##"]
notas.reverse()
if notas[0][0] == "F":
    notas.pop(0)
print(f"Notas transformadas: {notas}")

# 6. Matrices (más complejo)
matriz = [[1, 2], [3, 4]]
matriz_doble = [[x * 2 for x in fila] for fila in matriz]
matriz_doble.append([sum(matriz[0]), sum(matriz[1])])
for i in range(len(matriz_doble)):
    print(f"Fila {i}: {matriz_doble[i]}")

# 7. Matrices - Planetas (más complejo)
planetas = [["Mercurio", "Venus", "Tierra"], ["Marte", "Júpiter", "Saturno"], ["Urano", "Neptuno", "Plutón"]]
planetas[0], planetas[2] = planetas[2], planetas[0]
planetas[1] = [p.upper() for p in planetas[1] if len(p) > 4]
planetas[1:1] = [["Sol"]]
planetas = [fila for fila in planetas if fila]
for i, fila in enumerate(planetas):
    print(f"Grupo {i + 1}: {fila}")