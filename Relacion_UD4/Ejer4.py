#Ejercicio 4. Crea una lista con 10 números (los que quieras). Muestra por pantalla la media de dichos números. 
total = 0
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in numeros:
    total += n

media = total / len(numeros)
print(media)
print(f"La media es {(sum(numeros) / len(numeros))}")