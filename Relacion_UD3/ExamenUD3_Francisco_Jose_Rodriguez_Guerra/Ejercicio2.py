#Ejercicio 2 (5 puntos). Crea un programa que lea palabras por teclado y muestre por pantalla el número de letras de cada palabra leída.

palabra = ""

while True:
    try:
        palabra = input("Ingresa una palabra: ")
        if palabra.isnumeric():
            print("Debes introducir letras.")
            break
        print(len(palabra))
    except ValueError:
        print("No has introducido un valor valido.")
    except Exception as error:
        print(f"Error: {error}")