print("Determinar si las 3 longitudes de lados pueden crear un triangulo valido")
lado1 = float(input("Introduce el primer lado: "))
lado2 = float(input("Introduce el segundo lado: "))
lado3 = float(input("Introduce el tercer lado: "))
if (lado1+lado2)>lado3:
    print("Se puede crear un triangulo")
else:
    print("No se puede crear un triangulo")