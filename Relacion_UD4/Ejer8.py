#Ejercicio 8. Dada la siguiente lista con las precipitaciones en Granada mensuales del año 2023:
precipitaciones_granada_2023 = [
   40.2,  # Enero
   35.6,  # Febrero
   45.8,  # Marzo
   50.1,  # Abril
   30.3,  # Mayo
   10.4,  # Junio
   1.2,   # Julio
   5.6,   # Agosto
   20.8,  # Septiembre
   60.5,  # Octubre
   55.3,  # Noviembre
   42.7   # Diciembre
]
total = 0

for mes in precipitaciones_granada_2023:
    total += mes

media = total / len(precipitaciones_granada_2023)
print(f"La precicipitacion media de Granada es: {round(media, 2)}")
