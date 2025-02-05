num_total = 0
num_veces = 0
num_min = 0
num_max = 0
while True:
    num = int(input("Inserta un numero(0 para salir)"))
    if num == 0:
        break
    num_total = num_total + num
    num_veces += 1   
    if num_max < num:
        num_max = num
    if num_min > num or num_min == 0:
        num_min = num
media = num_total/num_veces
print(f"La media es {media}")
print(f"Numero minimo: {num_min}")
print(f"Numero maximo: {num_max}")