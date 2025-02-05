print("Que area quieres calcular")
print("1.Area de un triangulo")
print("2.Area de un rectangulo")
print("3.Area de un circulo")
opcion =int(input())

if opcion == 1 or opcion == 2:
    base = float(input("Introduce la base: "))
    altura = float(input("Introduce la altura: "))
elif opcion == 3:
    radio = float(input("Introduce el radio: "))
if opcion == 1:
    print(f"El area del triangulo es: {base*altura/2}cm^2")
elif opcion == 2:
    print(f"El area del rectangulo es: {base*altura}cm^2")
elif opcion == 3:
    print(f"El area del circulo es: {3.14*(radio*radio)}cm^2")