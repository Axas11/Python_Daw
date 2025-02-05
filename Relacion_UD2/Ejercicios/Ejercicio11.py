edad = int(input("Dime tu edad: "))
if edad<=2:
    print("Bebe")
elif edad>=3 and edad<=12:
    print("Nino")
elif edad>=13 and edad<=17:
    print("Adolescente")
elif edad>=18 and edad<=34:
    print("Adulto pero no")
elif edad==35:
    print("La mejor edad posible")
elif edad>=36 and edad<=50:
    print("Adulto")
elif edad>=51 and edad<=67:
    print("pre-anciano")
elif edad>=68 and edad<=99:
    print("Anciano")
elif edad==100:
    print("Centenario")