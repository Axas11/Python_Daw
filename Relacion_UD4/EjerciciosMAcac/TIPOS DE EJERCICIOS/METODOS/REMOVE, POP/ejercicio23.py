# Crea un programa que permita insertar números naturales* en una lista.  Cada vez que insertes un número deberá mostrar la lista entera. Si se inserta un número negativo deberá eliminar la primera aparición de su análogo positivo de la lista, es decir si inserto -3 significa “elimina el primer tres insertado”

nums = []
while True:
    num = int(input("Inserta un número: "))
    if num == 0: 
        break
    if num > 0:
        nums.append(num)
        print(f"Números introducidos: {nums}")
    elif num <0:
        if -num in nums:
            nums.remove(-num)
        print(f"Números introducidos: {nums}")
