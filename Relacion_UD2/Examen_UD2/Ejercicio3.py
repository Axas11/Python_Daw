preciobase = 0
tipo = input("Introduce el tipo de pista(tenis, futbol sala, futbol 11, rugby): ")
dia = input("Que dia quieres contratar la pista(L, M, X, J, V, S, D): ")
focos = input("Quieres focos para iluminar la pista(S/N)")
descuento = str(input("Eres estudiante de la UGR(S/N): "))

if dia == "S" or dia == "D":
    if tipo == "tenis":
        preciobase = 10
    elif tipo == "futbol sala":
        preciobase = 30
    elif tipo == "futbol 11":
        preciobase = 79
    elif tipo == "rugby":
        preciobase = 94
elif dia == "L" or dia == "M" or dia == "X" or dia == "J" or dia == "V":
    if tipo == "tenis":
        preciobase = 8
    elif tipo == "futbol sala":
        preciobase = 26
    elif tipo == "futbol 11":
        preciobase = 64
    elif tipo == "rugby":
        preciobase = 80

if focos == "S":
    if tipo == "tenis":
        preciobase = preciobase + 5
    elif tipo == "futbol sala":
        preciobase = preciobase + 10
    elif tipo == "futbol 11":
        preciobase = preciobase + 20
    elif tipo == "rugby":
        preciobase = preciobase + 25

if descuento == "S":
    RESTA = preciobase * 15 / 100
    preciobase -= RESTA

print(f"Pagarias un total de {preciobase} euros")