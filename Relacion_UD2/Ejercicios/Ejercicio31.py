while True:
    print("Elige la opcion por numeros: ")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Division")
    print("5.Division entera")
    print("6.Modulo(Resto de 2 numeros)")
    opt = input()

    if opt == "fin":
        break

    num1 = int(input("Introduce el primer numero: "))
    num2 = int(input("Introduce el segundo numero: "))

    match opt:
        case "1":
            print(f"{num1} + {num2} = {num1+num2}")
        case "2":
            print(f"{num1} - {num2} = {num1-num2} ")
        case "3":
            print(f"{num1} * {num2} = {num1*num2}")
        case "4":
            print(f"{num1} / {num2} = {num1/num2}")
        case "5":
            print(f"{num1} // {num2} = {num1//num2}")
        case "6":
            print(f"{num1} % {num2} = {num1%num2}")