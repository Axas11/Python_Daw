contador = 0

while True:
    palabra = input("Inserta una palabra: ")

    if palabra == "fin":
        break

    if len(palabra) <= 5:
        contador += 1

print(f"Hay {contador} palabras con menos de 5 caract")