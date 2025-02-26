# Simula una pila (stack) LIFO
pila = []
pila.append("tarea1")
pila.append("tarea2")
pila.append("tarea3")
while pila:
    print(f"Realizando: {pila.pop()}")