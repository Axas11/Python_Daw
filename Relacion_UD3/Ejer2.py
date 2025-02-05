def celsius2fahrenheit(grados: float) -> float:
    return grados*9/5+32

def fahrenheit2celsius(grados: float) -> float:
    return (grados-32)*5/9

try:
    base = float(input("Inserta una temperatura:"))
    altura = float(input("Inserta el tipo:"))
except ValueError as error:
    print(f"Valor no valido: {error}")
except Exception as error:
    print(f"Error: {error}")
else:
    if tipo == "Celsius":
        conversion = celsius2fahrenheit(temp)
        print(f"{temp} Celsius son {conversion} Fahrenheit")
    elif tipo == "fahrenheit":
        conversion = fahrenheit2celsius(temp)
        print(f"{temp} Fahrenheit son {conversion} Celsius")
    else:
        print("Tipo de temperatura desconocida")