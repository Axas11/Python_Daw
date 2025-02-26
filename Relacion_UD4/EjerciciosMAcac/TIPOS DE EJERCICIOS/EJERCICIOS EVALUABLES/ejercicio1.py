# Crea un programa que muestre por pantalla:
# La población media de dichos países.
# El nombre del país menos poblado.

paises = ["Alemania", "Francia", "Italia", "España", "Países Bajos", "Polonia", "Suecia", "Bélgica", "Austria", "Portugal"]

poblaciones = [83, 68, 59, 47, 17, 38, 10, 11, 9, 10]  # En millones de habitantes

menor_poblacion = poblaciones[0]
media= sum(poblaciones)/len(poblaciones)
print(f"La población media de los países es: {media} millones")

for n in poblaciones:
    if n < menor_poblacion:
        menor_poblacion = n

print(f"El país menos poblado es: {paises[poblaciones.index(menor_poblacion)]}")