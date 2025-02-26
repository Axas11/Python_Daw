# Crea un programa que lea números hasta que insertes un 0. Al terminar de leer números deberá mostrar por pantalla aquellos números insertados que sean superiores a la media. 
nums = []
numsMayores = []
total = 0
mayor = 0
while True:
    num = int(input("Inserta un número (0 para terminar): "))
    if num == 0:
        break
    nums.append(num)

for num in nums:
    total += num
media = total/len(nums)

for num in nums:
    if num > media:
        mayor = num
        numsMayores.append(mayor)

print(f"La lista de números es: {nums}")
print(F"La media es: {round(media, 2)}")
print(f"Los números insertados mayores que la media son: {numsMayores}")
