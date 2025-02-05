num_secreto = 42
n_intentos = 0
try:
    num = int(input("Inseta un numero: "))
except Exception as error:
    print('Se ha producido un error')
else:
    if num == num_secreto:
        print("Acertaste!!")
    elif num < num_secreto:
        print("El num secreto es mayor")
    else:
        print("El num secreto es menor")
    
    