via = input("Elige el tipo de via: (autovia o nacional): ")
vehiculo = input("Elige el vehiculo: (coche, autobus o camion): ")
if via == "autovia":
    if vehiculo == "coche":
        print("Puedes conducir a 120km/h")
    elif vehiculo == "autobus":
        print("Puedes conducir a 110km/h")
    else:
        print("Puedes conducir a 100km/h")
else:
    if vehiculo == "coche" or vehiculo == "autobus":
        print("Puedes conducir a 100km/h")
    else:
        print("Puedes conducir a 90km/h")

