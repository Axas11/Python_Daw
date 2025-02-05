via = (input("Elige el tipo de via: (Nacional o Autovia): "))
vehiculo = (input("Elige el tipo de vehiculo: (Coche, Bus o Camion): "))
            
velocidadMax = 0

if via == "Autovia":
    if vehiculo == "Coche":
        velocidadMax = 120
    elif vehiculo == "Bus":
        velocidadMax = 110
    elif vehiculo == "Camion":
        velocidadMax = 100
elif via == "Nacional":
    if vehiculo == "Coche" or vehiculo == "Bus":
        velocidadMax = 100
    elif vehiculo == "Camion":
        velocidadMax = 90

print(f"El tipo de vehiculo {vehiculo} por el tipo de vía {via} puede ir como máximo a {velocidadMax}")