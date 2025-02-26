# Crea un programa que inserte números en una lista hasta introducir el número 0. A continuación deberá mostrar en pantalla todos los números introducidos en orden inverso, es decir primero el último número introducido. 
nums = []
while True:
    num = int(input("Inserta un número: ( 0 para terminar) "))
    if num == 0:
        break
    nums.append(num)
    print(nums)
while nums:
    print(nums.pop())