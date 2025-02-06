#Ejercicio 3. Crea una lista con 10 numeros (los que quieras pero que no esten ordenados). 
#Muestra por pantalla solo aquellos numeros que sean mayores al primero. 
num_min = 0
num_max = 0

numeros = ["20", "30", "50", "10", "200", "1", "14", "200" , "9", "102"]
primero = numeros[0]
print(f"El primer número es: {primero}")
print("Números mayores al primero:")
for numero in numeros:
    if primero < numero:
        print(numero)




