#Ejercicio 1 (5 puntos). Crea un programa que lea dos números por teclado y muestre el resultado de dividirlo. 

num1 = 0
num2 = 0
resultado = 0

while True:
    try:
        num1 = float(input("Ingresa el primer numero que desees dividir: "))
        num2 = float(input("Ingresa el segundo numero que desees dividir: "))
        resultado = num1/num2
    except ZeroDivisionError as error:
        print("No se puede dividir entre 0.")
    except ValueError as error:
        print("Debes introducir un")
    except Exception as error:    
        print(f"Error: {error}")
    else:
        print(f"{num1} entre {num2} = {resultado}")