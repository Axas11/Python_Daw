print("Adivina el numero secreto...")
num = float(input("Cual crees que es: "))
numsec = 24
intentos = 0
while numsec != num:
    num = float(input("Cual crees que es: "))
    intentos = intentos + 1
print(f"Felicidades, has acertado el numero secreto {numsec}")
print(f"Con un total de {intentos} intentos")