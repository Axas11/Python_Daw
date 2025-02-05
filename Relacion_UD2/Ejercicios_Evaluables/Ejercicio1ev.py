cant=0
suma=0
media=0
nummax=0
nummin=0
while suma<=100:
    num=int(input("Introduce un numero: "))
    if nummin==0:
        nummin=num
    if num<nummin:
        nummin=num
    if num>nummax:
        nummax=num
    suma=suma+num
    print(suma)
    cant+=1
media=suma/cant
print(f"La cantidad de numeros: {cant}")
print(f"La suma es: {suma}")
print(f"La media es: {media}")
print(f"El numero mayor es: {nummax}")
print(f"El numero menor es: {nummin}")