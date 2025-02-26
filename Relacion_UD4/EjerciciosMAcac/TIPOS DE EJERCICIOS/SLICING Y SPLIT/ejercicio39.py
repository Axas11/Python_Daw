# Crea un programa en el que insertes palabras separados por comas:
#El programa deberá mostrar la palabras más corta y larga:

palabra = input("Inserta palabras separadas por comas: ")
lista_palabras = palabra.split(",")
palabra_menor = lista_palabras[0]
palabra_mayor = lista_palabras[0]
print(lista_palabras)
for palabra in lista_palabras:
    if len(palabra) > len(palabra_mayor):
        palabra_mayor = palabra
    elif len(palabra) < len(palabra_menor):
        palabra_menor = palabra
print(f"La palabra con menos letras es: {palabra_menor}")
print(f"La palabra con más letras es: {palabra_mayor}")