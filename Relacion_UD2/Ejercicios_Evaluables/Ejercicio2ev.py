import random

pares = 0
impares = 0
i = 0
while i < 10:
    numero = random.randint(20, 40)
    print(numero)
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    i += 1

print("Numeros pares: ",pares)
print("Porcentaje: ",pares*100/10,"%")
print("Impares: ",impares)
print("Impares: ",impares*100/10,"%")