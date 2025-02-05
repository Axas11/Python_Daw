peso = float(input("Inserta el peso de tu coche: (en KG)"))

if peso < 1000:
    print("Es un coche ligero")
elif peso >= 1000 and peso <= 2000:
    print("Es un coche mediano")
else:
    print("Es un coche pesado")