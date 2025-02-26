import statistics
# Halla la nota media de toda la clase
matriz = [
    ["Juanillo", 4, 1, 5],
    ["staryuki", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]
valores = [n[1:] for n in matriz ]
media_total = 0

for fila in matriz:
    for elemento in fila:
        notas = fila[1:]
        media = sum(notas)/ len(notas)
    media_total += media / len(matriz)
print(f"La media total de la clase es: {media_total}")