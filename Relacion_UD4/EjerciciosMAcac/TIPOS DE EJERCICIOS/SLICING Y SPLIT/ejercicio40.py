# Crea un programa que lea números separados por un punto y coma. El programa deberá mostrar:
# El número mayor
# El número menor
# La suma de todos los números
# La media
import statistics
numeros = input("Inserta números separados por ; --> ")
lista_numeros = numeros.split(";")
for i in range(len(lista_numeros)):
    lista_numeros[i] = int(lista_numeros[i])
print(lista_numeros)
print(f"El número mayor es : {max(lista_numeros)}")
print(f"El número menor es: {min(lista_numeros)}")
print(f"La suma es: {sum(lista_numeros)}")
print(f"La media es: {statistics.mean(lista_numeros)}")