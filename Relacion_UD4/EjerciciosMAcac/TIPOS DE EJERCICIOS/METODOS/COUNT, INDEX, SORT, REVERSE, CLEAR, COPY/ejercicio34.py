# Crea un programa que lea números hasta que insertes un cero. Una vez se inserte el cero se mostrarán los números introducidos en orden inverso, es decir primero el último número introducido y al final el primero. 
nums = []
while True:
    n = int(input("Inserta un número (0 para terminar) "))
    if n == 0:
        break
    nums.append(n)
nums.reverse()
print(nums)