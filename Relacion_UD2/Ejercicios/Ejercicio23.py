print("Que quieres calcular")
print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")
opcion = input()

num1 = float(input("Introduce el primer numero"))
num2 = float(input("Introduce el segundo numero"))

match opcion:
    case "1":
       print(f"{num1} + {num2} = {num1+num2}")
    case "2":
        print(f"{num1} - {num2} = {num1-num2} ")
    case "3":
        print(f"{num1} * {num2} = {num1*num2}")
    case "4":
        print(f"{num1} / {num2} = {num1/num2}")
    case _:
        print("Posicion no correcta")
