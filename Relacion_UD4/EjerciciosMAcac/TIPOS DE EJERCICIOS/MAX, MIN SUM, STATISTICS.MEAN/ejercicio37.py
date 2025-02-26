# Crea un programa que lea números hasta que insertes un cero. Al finalizar el programa deberá mostrar:
# El mayor de los números introducidos
# El menor de los números introducidos
# La media de los números introducidos

import statistics
nums = []

while True:
    n = int(input("Inserta un número (0 para terminar)"))
    if n == 0:
        break
    nums.append(n)

print(f"El mayor de los números introducidos es: {max(nums)}")
print(f"El menor de los números introducidos es: {min(nums)}")
print(f"La media de los números introducidos es: {statistics.mean(nums)}")
