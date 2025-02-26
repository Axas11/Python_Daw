# Halla la nota media de cada alumno
matriz = [
    ["Juanillo", 4, 1, 5],
    ["staryuki", 9, 10, 9],
    ["Ramoncín", 1, 5, 1],
    ["Gerardo", 5, 5, 5],
    ["Einstein", 10, 10, 10]
]

valores = [n[1:] for n in matriz ]

for i,fila in enumerate(valores):
    print(f"La media de {matriz[i][0]} es : {round(sum(fila)/len(fila),2)}")

#Solucion VICTOR
# for fila in matriz:
#     print(sum(fila[1:])/len(fila[1:]))
