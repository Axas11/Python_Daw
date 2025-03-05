#Crea un programa que muestre por pantalla:
#La población media de dichos países.
#El nombre del país menos poblado.

paises = ["Alemania", "Francia", "Italia", "España", "Países Bajos", "Polonia", "Suecia", "Bélgica", "Austria", "Portugal"]

poblaciones = [83, 68, 59, 47, 17, 38, 10, 11, 9, 10]  # En millones de habitantes

poblacion = 0
menor_poblacion = poblaciones[0]  
posicion_minima = 0  

poblacion = sum(poblaciones) / len(poblaciones)

for posicion in range(len(poblaciones)):
    if poblaciones[posicion] < menor_poblacion:
        menor_poblacion = poblaciones[posicion] 
        posicion_minima = posicion

pais_menos_poblado = paises[posicion_minima]

print(f"Poblacion media: {poblacion}")
print(f"Pais menos poblado: {pais_menos_poblado}")