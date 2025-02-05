contador = 1
palabraCorta = ""
palabraLarga = ""
while True:
    palabra = input("Inserta una palabra: ")
   
    if palabra == "fin":
        break
    
    if contador == 1:
        palabraCorta = palabra
        palabraLarga = palabra
    else:
        if len(palabra) > len(palabraLarga): 
            palabraLarga = palabra
        if len(palabra) < len(palabraCorta): 
            palabraCorta = palabra
    
    contador = contador + 1

print(f"La palabra mas corta es: {palabraCorta} y la mas larga es {palabraLarga}")