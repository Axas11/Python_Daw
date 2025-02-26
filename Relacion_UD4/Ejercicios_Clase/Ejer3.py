#Ejercicio 3. Crea una lista con 10 numeros (los que quieras pero que no esten ordenados). 
#Muestra por pantalla solo aquellos numeros que sean mayores al primero. 
numeros = [20, 30, 50, 10, 200, 1, 14, 201, 9, 102]

print(f"El primer número es: {numeros[0]}")
print("Números mayores al primero:")

for mayor in numeros:
    if numeros[0] < mayor:
        print(mayor)




