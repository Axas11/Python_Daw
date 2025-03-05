#Crea una función que dadas una lista de números y un número n determine si todos los números de la lista son mayores o iguales a n. 
#La función deberá devolver True o False.  

def todos_mayores_o_iguales(lista_numeros, n):
    for numero in lista_numeros:
        if numero < n:
            return False
    return True

numeros1 = [5, 7, 9, 10]

n = 5

print(f"Dada la lista: {numeros1}")
print(f"El valor de n es: {n}")
print(todos_mayores_o_iguales(numeros1, n))
