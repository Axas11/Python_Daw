dia = input("Inserta un dia de la semana(L, M, X, J, V, S, D): ")
hab = input("Selecciona tipo de hab (individual o doble): ")
festivo = input("Dime si el dia es festivo (si o no): ")
cupon = input("Tienes cupon (si o no): ")
if cupon == "si":
    porcentajecupon = float(input("Inserta el portecentaje del cupon: "))

if dia == "D" and festivo == "no":
    precio = 40 if hab == "individual" else 60
elif dia == "V" or dia == "S" or festivo == "si":
    precio = 45 if hab == "individual" else 70
else:
    precio = 30 if hab == "individual" else 50

if cupon == "si":
    descuento = precio * porcentajecupon / 100
    precio -= descuento

print(f"El precio es: {precio}")
