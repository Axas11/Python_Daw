import statistics
# Halla el alumno cuya nota media sea la más baja
matriz = [
    ["Juanillo", 4, 1, 5],
    ["staryuki", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]

valores = [n[1:] for n in matriz ]
media_baja = statistics.mean(valores[0])

for i, fila in enumerate(valores):
    if statistics.mean(valores[i]) < media_baja:
        media_baja = statistics.mean(valores[i])
        print(f"La media mas baja es la de: {matriz[i][0]} con una media de: {round(media_baja,2)}")