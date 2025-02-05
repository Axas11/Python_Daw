#Ejercicio 8. Crea un programa que dada la longitud de los dos catetos de un triángulo rectángulo obtenga la hipotenusa. 
#Recuerda el teorema de Pitágoras → h2 = c12+c22 o lo que es lo mismo h = math.sqrt( c12+c22 ). Una vez creada comprueba que funciona.
import math

c1 = 0
c2 = 0
hipotenusa = 0

while True:
    try:
        c1=float(input("cateto 1: "))
        c2=float(input("cateto 2: "))

    except ValueError:
        print("Error: Debes introducir un numero valido.")
    except Exception as error:
        print(f"Se ha producido un error: {error}")

    else:
        hipotenusa=math.sqrt(c1**2+c2**2)
        print(f"La hipotenusa es: {hipotenusa:.2f}")

