print("Este programa determina si tu triangulo es equilatero, isosceles o escaleno")
lado1 = float(input("Dime la longitud de el primer lado"))
lado2 = float(input("Dime la longitud de el segundo lado"))
lado3 = float(input("Dime la longitud de el tercer lado"))

if lado1 == lado2 == lado3:
    print("Es un trinagulo equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Es un triangulo isosceles")
else:
    print("Es un triangulo escaleno")