import random

nPares = nImpares = 0

for _ in range(10):
    aleatorio = random.randint(20,40)
    print(aleatorio)

    if aleatorio % 2 == 0:
        nPares += 1
    else:
        nImpares += 1
        
porcentajePares = nPares / 10 * 100
porcentajeImpares = nImpares / 10 * 100
print(f"Un {porcentajePares}% son pares y un {porcentajeImpares}% son impares")