#Dada una matriz como la siguiente (columna 2 son el número de habitantes y la 4 el área):
#Crea una función que recibido un continente y la lista de países devuelva el país con mayor densidad de población (población/área).
paises = [
    ["Argentina", "Buenos Aires", 46000000, "America", 2780400],  
    ["España", "Madrid", 48000000, "Europa", 505990],  
    ["Japón", "Tokio", 125000000, "Asia", 377975],  
    ["Sudáfrica", "Pretoria", 60000000, "África", 1221037],  
    ["Australia", "Canberra", 26000000, "Oceanía", 7692024],  
    ["Canadá", "Ottawa", 38000000, "América", 9984670]  
]

def mayor_densidad(continente, lista_paises):
    max_densidad = 0
    pais_max = ""
    
    for pais in lista_paises:
        if pais[3] == continente:
            densidad = pais[2] / pais[4]  
            if densidad > max_densidad:
                max_densidad = densidad
                pais_max = pais[0]
    
    return pais_max

print(mayor_densidad("America", paises))

