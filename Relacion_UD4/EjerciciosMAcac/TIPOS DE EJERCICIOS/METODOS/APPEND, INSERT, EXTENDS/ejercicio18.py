# Escribe un programa que genere una lista con los pares comprendidos entre a y b. Los parámetros a y b son leídos desde el teclado. (Hacerlo sin listas y con listas)
numeros = []
a = int(input("Inserta un número para a (Será el valor de inicio): "))
b = int(input("Inserta un número para b (Será el valor de fin): "))
while True:
    n = int(input("Inserta un número (0 para terminar): "))
    if n == 0:
        break
    if n >= a and n <= b and n % 2 == 0:
        numeros.append(n)
print(numeros)
