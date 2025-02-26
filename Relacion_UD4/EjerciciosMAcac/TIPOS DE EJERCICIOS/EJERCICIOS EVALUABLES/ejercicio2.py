#Crea una función que dadas una lista de números y un número n determine si todos los números de la lista son mayores o iguales a n. 
# La función deberá devolver True o False.  

def mostrar_nums(numeros:list, n:int)->bool:
    for num in numeros:
        if num <= n:
            return False
    return True


numeros = [17, 82, 45, 29, 73, 56, 91, 38, 64, 10]
n = 11

nums = mostrar_nums(numeros,n)
print(f"Todos los numeros de la lista son mayores o iguales que {n}?? {nums}")