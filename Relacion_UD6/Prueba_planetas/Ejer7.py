#Ejercicio 7. A partir de la lista creada en el ejercicio 6:
#Crea una lista con las densidades de todos los planetas
#Obtén el planeta cuya densidad sea mayor
#Encuentra las lunas que sean más grandes que la Luna
#Encuentra la luna más pequeña

from Planeta import Planeta
from datetime import datetime

planetas = [
    Planeta("Mercurio", 3.301e23, 2.4397e6, datetime.min, []),
    Planeta("Venus", 4.867e24, 6.0518e6, datetime.min, []),
    Planeta("Tierra", 5.972e24, 6.371e6, datetime.min, [["Luna", 1.737e6, 7.342e22]]),
    Planeta("Marte", 6.417e23, 3.3895e6, datetime.min, [["Fobos", 1.1e4, 1.0659e16], ["Deimos", 6.2e3, 1.4762e15]]),
    Planeta("Jupiter", 1.898e27, 6.9911e7, datetime.min, [["Ganimedes", 2.634e6, 1.4819e23], ["Calisto", 2.410e6, 1.0759e23], 
                                                          ["Ío", 1.821e6, 8.9319e22], ["Europa", 1.560e6, 4.7998e22]]),
    Planeta("Saturno", 5.683e26, 5.8232e7, datetime.min, [["Titan", 2.575e6, 1.3452e23], ["Rea", 1.527e6, 2.3166e21], 
                                                          ["Japeto", 1.470e6, 1.8056e21], ["Dione", 1.123e6, 1.0955e21]]),
    Planeta("Urano", 8.681e25, 2.5362e7, datetime.min, [["Titania", 1.578e6, 3.527e21]]),
    Planeta("Neptuno", 1.024e26, 2.4622e7, datetime.min, [["Triton", 1.353e6, 2.14e22]]),
    Planeta("Pluton", 1.303e22, 1.1883e6, datetime(1930, 2, 18), [["Caronte", 6.057e5, 1.586e21]])
]
for planeta in planetas:
    print(f"Nombre: {planeta.nombre} Densidad: {planeta.get_densidad()}")

densidades = [planeta.get_densidad() for planeta in planetas]
mayor_densidad = max(densidades)
planeta_mayor_densidad = [planeta for planeta in planetas if planeta.get_densidad() == mayor_densidad][0]
print(planeta_mayor_densidad)

#Encuentro el radio de la luna
radio_luna = 0
for planeta in planetas:
    for luna in planeta.lunas:
        if luna[0] == "Luna":
            radio_luna = luna[1]
            break
print(f"{radio_luna}")
#Encuentro la luna mas grande que la luna
lunas_grandes = []
for planeta in planetas:
    for luna in planeta.lunas:
        if luna[1] > radio_luna:
            lunas_grandes.append(luna[0])

print(f"Las lunas mas grandes que la luna son: {lunas_grandes}")

#Encuentra la luna mas pequeña
radios_luna = []
for planeta in planetas:
    for luna in planeta.lunas:
        radios_luna.append(luna[1])

radio_min= min(radios_luna)

for planeta in planetas:
    for luna in planeta.lunas:
        if luna[1] == radio_min:
            print(f"La luna mas peque es: {luna[0]}")
            
