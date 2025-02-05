suma = nNumeros = media = mayor = menor = 0
while suma < 100:
    num = int(input("Inserta un numero: "))
    if nNumeros == 0:
        mayor = num
        menor = num
    else:
        if num > mayor:
            mayor = num
        
        if num < menor:
            menor = num
    
    
    suma += num
    nNumeros += 1
media = nNumeros/suma
print(f"Cantidad de numero introducidos: {nNumeros}")
print(f"Suma total: {suma}")
print(f"Media: {media}")
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")
    