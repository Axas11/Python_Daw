# Escribe un programa que genere una lista con los pares comprendidos entre a y b. Los parámetros a y b son leídos desde el teclado. (Hacerlo sin listas y con listas)
a = int(input("Inserta un número para a (Será el valor de inicio): "))
b = int(input("Inserta un número para b (Será el valor de fin): "))
for i in range(a, b+1):
    if i % 2 == 0:
        print(i)
