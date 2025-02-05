def mostrar_multiplos(n, inicio, final):
    for i in range(inicio, final + 1):
        if i % n == 0: 
            print(i)
numero = int(input("Introduce un num: "))
inicio = int(input("Introduce el inicio "))
final = int(input("Introduce el final: "))

mostrar_multiplos(numero, inicio, final)