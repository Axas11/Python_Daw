#Ejercicio 9. Crea un programa que simule el juego “pares o nones”. Primero eliges entre pares o nones y después eliges cuantos dedos sacas. 
#A continuación la máquina decide, de forma aleatoria, cuántos dedos saca y se comprueba quién ha ganado.
import random

pares = 0
nones = 0
bot = 0
total_dedos = 0
resultado = 0

while True:
    try:
        print("PARES O NONES")
        option = int(input("Elige entre pares = 1 o nones = 2: "))
        if option not in [1, 2]:
            print("Tienes que elegir entre 1 y 2")
            continue 

        bot = random.randint(0, 10)

        dedos = int(input("Saca de 0 a 10 dedos: "))
        if dedos not in range(0, 11):
            print("Dedos entre 0 y 10.")
            continue 

        print(f"La máquina sacó {bot} dedos.")
        total_dedos = dedos + bot
        print(f"Suma total de dedos: {total_dedos}")

        if total_dedos % 2 == 0:  
            resultado = "pares"
        else:  
            resultado = "nones"

        if (resultado == "pares" and option == 1) or (resultado == "nones" and option == 2):
            print(f"Ganaste!, {resultado}")
        else:
            print(f"Perdiste, {resultado}")

        break  

    except ValueError:
        print("Error: Debes introducir un numero valido.")
    except Exception as error:
        print(f"Se ha producido un error: {error}")
