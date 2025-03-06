def mostrar_palabra(palabra, letras_adivinadas):

    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "

    if resultado:
        resultado = resultado[:-1]  
    return resultado

def letra_valida(letra, letras_usadas):

    if len(letra) != 1:  
        return False
    if letra in letras_usadas:  
        return False
    return True

def palabra_completa(palabra, letras_adivinadas):

    for letra in palabra:
        if letra not in letras_adivinadas:
            return False
    return True