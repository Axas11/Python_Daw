#Crea un programa que lea números hasta que insertes un cero. A continuación te volverá a pedir un número n y mostrará los últimos n número introducidos. 

nums = []

while True:
    n = int(input("Inserta un número (0 para terminar) "))
    if n == 0:
        break
    nums.append(n)
num_ultimo = int(input("Cuantos números quieres mostrar? "))
nums.reverse()

print(f"Los últimos {num_ultimo} números son: ")
for i in range(num_ultimo):
    print(nums[i])