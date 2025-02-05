print("Que quieres calcular?")
print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")
opcion = int(input())

num1 = float(input("Introduce el primer numero"))
num2 = float(input("Introduce el segundo numero"))

if opcion == 1:
    print(f"{num1} + {num2} = {num1+num2}")
elif opcion == 2:
    print(f"{num1} - {num2} = {num1-num2} ")
elif opcion == 3:
    print(f"{num1} * {num2} = {num1*num2}")
elif opcion == 4:
    print(f"{num1} / {num2} = {num1/num2}")