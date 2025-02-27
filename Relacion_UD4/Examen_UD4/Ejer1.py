#Ejercicio 1 (1 punto). Dadas las siguientes listas:
#Encuentra (utilizando bucles, condicionales y/o métodos/funciones de las listas):
#El nombre del animal que menos pesa
#El nombre de los animales que pesan más que la media.

animales_domesticos = ["Perro", "Gato", "Conejo", "Hámster", "Loro", "Pez", "Tortuga", "Cobaya", "Hurón", "Canario"]
pesos_animales = [10, 4, 2, 0.1, 0.3, 0.2, 1.5, 1, 1.2, 0.05]

suma_pesos = 0
peso_minimo = pesos_animales[0]
animal_menos_pesado = animales_domesticos[0]


contador = 0
for peso in pesos_animales:
    if peso < peso_minimo:
        peso_minimo = peso
        animal_menos_pesado = animales_domesticos[contador]
    contador += 1


for peso in pesos_animales:
    suma_pesos = suma_pesos + peso
media_pesos = suma_pesos / len(pesos_animales)


animales_mayor_media = []
contador = 0
for peso in pesos_animales:
    if peso > media_pesos:
        animales_mayor_media.append(animales_domesticos[contador])
    contador = contador + 1

print("Animal que menos pesa: ")
print(animal_menos_pesado)
print("Animales que pesan mas que la media: ")
for animal in animales_mayor_media:
    print(animal)


