letra = input("Introduce una letra, que quieras saber de la siguiente palabra: ")
contador = 0
palabra = ""
while palabra != "fin":
    palabra = input("Introduce una palabra, fin para terminar: ")
    if palabra != "fin":
        for caracter in palabra:
            if caracter == letra:
                contador += 1

print(f"La letra '{letra}' aparece {contador} ")