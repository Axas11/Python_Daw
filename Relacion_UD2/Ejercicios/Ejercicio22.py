dia = input("Que dia de la semana deseas viajar: ")
hora = int(input("A que hora del dia deseas viajar: "))
km = float(input("Cuantos kilometros vas a recorrer: "))
if dia == "lunes" or dia == "martes" or dia == "miercoles" or dia == "jueves" or dia == "viernes":
    if hora>= 8 and hora<= 18:
        tarifa = 1
    elif hora>= 19 and hora<= 23:
        tarifa = 1.2
    else: #23 y 7
        tarifa = 1.5
elif dia == "sabado":
    if hora>= 8 and hora<= 18:
        tarifa = 1.2
    else: #resto del dia
        tarifa = 1.5
else: #Domingo
    tarifa = 1.5
total = 3.5 + (tarifa*km)
print(f"El dia {dia}, a las {hora} tendra un coste total de {total} euros")