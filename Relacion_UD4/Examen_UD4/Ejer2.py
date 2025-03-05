#Ejercicio 2 (1 punto). Dadas las siguientes listas:
#En las que la segunda lista representa el peso mínimo y el máximo para cada animal, 
#encontrar el nombre del animal con la diferencia entre su menor y mayor peso más grande. 
animales_domesticos = ["Perro", "Gato", "Conejo", "Hámster", "Loro", "Pez", "Tortuga", "Cobaya", "Hurón", "Canario"]

pesos_animales = [
    [5, 40],   # Perro (depende de la raza)
    [2, 8],    # Gato
    [1, 3],    # Conejo
    [0.08, 0.25], # Hámster
    [0.2, 1.5],   # Loro
    [0.1, 2],  # Pez (varía mucho según la especie)
    [0.5, 2],  # Tortuga (pequeñas domésticas)
    [0.7, 1.5],  # Cobaya
    [0.5, 2],  # Hurón
    [0.02, 0.06] # Canario
]
  
mayor_diferencia = 0
animal_mayor_diferencia = ""

contador = 0

for peso in pesos_animales:
    diferencia = peso[1] - peso[0]
    if diferencia > mayor_diferencia:
        mayor_diferencia = diferencia
        animal_mayor_diferencia = animales_domesticos[contador]
    contador = contador + 1

print("El animal con la mayor diferencia de peso es:")
print(animal_mayor_diferencia)
