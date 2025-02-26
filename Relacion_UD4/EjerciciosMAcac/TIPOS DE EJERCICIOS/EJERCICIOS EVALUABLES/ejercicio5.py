# Crea una función que recibido un continente y la lista de países devuelva el país
# con mayor densidad de población (población/área).
paises = [
    ["Argentina", "Buenos Aires", 46000000, "América", 2780400],  
    ["España", "Madrid", 48000000, "Europa", 505990],  
    ["Japón", "Tokio", 125000000, "Asia", 377975],  
    ["Sudáfrica", "Pretoria", 60000000, "África", 1221037],  
    ["Australia", "Canberra", 26000000, "Oceanía", 7692024],  
    ["Canadá", "Ottawa", 38000000, "América", 9984670]  
]

continentes = [continente[3:4] for continente in paises]

def mayor_densidad(continente:str,paises:list)->int:
    densidad_max = 0
    pais_grande = 0
    for pais in paises:
        if pais[3] == continente:
            poblacion = pais[2]
            area = pais[4]
            densidad = poblacion/area
            if densidad > densidad_max:
                densidad_max = densidad
                pais_grande = pais[0]
    return pais_grande

continente = input("Inserta un continente: ")

print(mayor_densidad(continente,paises))