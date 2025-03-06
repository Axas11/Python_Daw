from Funciones import mostrar_palabra, letra_valida, palabra_completa

palabras = [
    "chivato",    
    "supercalifragilisticoespalidoso",  
    "boquerones" 
]

vidas = 10
nivel = 0
letras_adivinadas = []
letras_usadas = []

print("Bienvenido al juego del Ahorcado")

while nivel < 3 and vidas > 0:
    palabra_actual = palabras[nivel]
    print("Palabra que debes encontrar: ")
    
    while vidas > 0 and not palabra_completa(palabra_actual, letras_adivinadas):
        print("Vidas:", vidas)
        print(mostrar_palabra(palabra_actual, letras_adivinadas))
        print("Letras usadas:", letras_usadas)
        letra = input("Ingresa una letra: ").lower()
        
        if not letra_valida(letra, letras_usadas):
            print("Letra inválida o ya usada")
            continue
            
        letras_usadas.append(letra)
        
        if letra in palabra_actual:
            if letra not in letras_adivinadas:
                letras_adivinadas.append(letra)
                vidas += 1
                print("Ganaste una vida")
            else:
                print("Ya habias adivinado esa letra")
        else:
            vidas -= 1
            print("Perdiste una vida")
    
    if palabra_completa(palabra_actual, letras_adivinadas):
        print() 
        mensaje_felicidades = "Has completado el nivel "
        print(mensaje_felicidades, end="") 
        numero_nivel_completado = nivel + 1  
        print(numero_nivel_completado)  
        
        print("Palabra:", palabra_actual)
        nivel += 1
        letras_adivinadas = []
        letras_usadas = []
        
    if vidas <= 0:
        print("Te quedaste sin vidas")
        print("La palabra era:", palabra_actual)
        break

if nivel == 3:
    print("Has ganado el juego completo")
    print("Vidas restantes:", vidas)
