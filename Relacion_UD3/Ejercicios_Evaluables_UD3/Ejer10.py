#Ejercicio 10. Crea un programa que te pida dos números y que te muestre por pantalla todos los números que hay entre el menor de los números introducidos y el mayor.

num1 = 0
num2 = 0
inicio = 0
fin = 0
num_min = 0
num_max = 0
num = 0

while True:
    try:
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))

        if num_max < num1:
            num_max = num1
        if num_min > num1 or num_min == 0:
            num_min = num1
        
        if num_max < num2:
            num_max = num2
        if num_min > num2 or num_min == 0:
            num_min = num2

        inicio = num_min + 1  
        fin = num_max

        print(f"Los números entre {inicio-1} y {fin} son:")
        for num in range(inicio, fin):
            print(num)

    except ValueError:
        print("Error: Debes introducir un numero valido.")
    except Exception as error:
        print(f"Se ha producido un error: {error}")