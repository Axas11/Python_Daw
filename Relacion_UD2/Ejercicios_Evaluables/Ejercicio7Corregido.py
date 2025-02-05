nLetras = 0

letra = input("Inserta una letra: ")

while True:
    palabra = input("Inseta una palabra: ")

    if palabra == "fin":
        break

    for caracter in palabra:
        if letra == caracter:
            nLetras += 1

print(f"La letra '{letra}' aparece {nLetras} ")
