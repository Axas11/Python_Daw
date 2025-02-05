#Ejercicio 7. Crea un programa que resuelva ecuaciones de segundo grado a partir de los términos a, b y c. 
#El programa debe continuar hasta que el término a sea igual a 0.
import math

a = 0
b = 0
c = 0
discriminante = 0
sol1 = 0
sol2 = 0

def ecuacion(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return None, None
    sol1 = (-b + math.sqrt(discriminante)) / (2*a)
    sol2 = (-b - math.sqrt(discriminante)) / (2*a)
    return sol1, sol2

while True:
    try:
        a = float(input("Introduce el valor de a: "))
        if a == 0:
            print("a no puede ser 0.")
            break

        b = float(input("Introduce el valor de b: "))
        c = float(input("Introduce el valor de c: "))

        sol1, sol2 = ecuacion(a, b, c)

        if sol1 is None or sol2 is None:
            print("La ecuación no tiene soluciones reales.")
        else:
            print(f"Las soluciones son: {sol1} y {sol2}")

    except ValueError:
        print("Error: Debes introducir un numero valido.")
    except Exception as error:
        print(f"Se ha producido un error: {error}")