# Crea un programa que lea números hasta que insertes un cero. Una vez se inserte el cero se mostrarán los números introducidos de menor a mayor (el cero no debe contar). 
nums = []
while True: 
    n = int(input("Iserta un número (0 para terminar): "))
    if n == 0:
        break
    else:
        nums.append(n)

nums.sort()
print(nums)