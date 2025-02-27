#Ejercicio 4 (1 punto). Crea la función sin_repetidos(l: list) que dada una lista de números devuelva otra lista que contenga los números de la primera lista pero sin repeticiones. La lista original NO debe ser cambiada. 

def sin_repetidos(l: list):
    resultado = []
    for numero in l:
        if numero not in resultado:
            resultado.append(numero)
    return resultado

numeros = [1, 2, 2, 3, 3, 4, 4, 5]

sin_repetidos = sin_repetidos(numeros)

print(sin_repetidos)

