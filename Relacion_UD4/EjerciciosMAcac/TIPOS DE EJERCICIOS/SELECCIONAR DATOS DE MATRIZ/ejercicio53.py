# Halla los alumnos que tengan al menos una asignatura suspensa
matriz = [
    ["Juanillo", 4, 1, 5],
    ["staryuki", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]

valores = [n[1:] for n in matriz ]
print("Los alumnos que tienen al menos una asignatura suspensa son: ")
for i, fila in enumerate(valores):
    for nota in fila:
        if nota < 5:
            print(f"{matriz[i][0]}")
        break