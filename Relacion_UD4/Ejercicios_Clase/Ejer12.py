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

max_precipitacion = precipitaciones_granada_2023[0]
mes_max = 0

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

for i, precipitacion in enumerate(precipitaciones_granada_2023):
    if precipitacion > max_precipitacion:
        max_precipitacion = precipitacion
        mes_max = i

print(f"El mes que más ha llovido es: {meses[mes_max]} con {max_precipitacion} mm")
