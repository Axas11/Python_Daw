mult = int(input("Introduce el numero, se creara la tabla de el numero que introduzas: "))
contador = 0
while contador < 10:
    tabla = mult * contador
    contador = contador + 1
    print(f"{mult} x {contador} = {tabla}")