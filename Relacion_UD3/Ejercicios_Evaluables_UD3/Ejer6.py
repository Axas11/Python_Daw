#Ejercicio 6. Crea un programa que lea tres variables: inicio, fin y nVeces. Pudiendo ser inicio y fin números reales. El programa deberá crear <nVeces> números reales aleatorios entre <inicio> y <fin> redondeados a dos cifras decimales. 
import random

inicio = 0
fin = 0
nVeces = 0
numero = 0

while True:
    try:
        inicio = float(input("Inicio: "))
        fin = float(input("Fin: "))
        nVeces = int(input("Cantidad de numeros: "))

        print("Numeros generados:")
        for _ in range(nVeces):
            numero = round(random.uniform(inicio, fin), 2)
            print(numero)
        break
    except ValueError:
        print("Error: Debes introducir un numero valido.")
    except Exception as error:
        print(f"Se ha producido un error: {error}")