temp = float(input("Ingresa la temperatura: "))
unidad = input("Ingresa la unidad: (Celsius o Fahrenheit)")
if unidad == "Celsius" or unidad == "celsius":
    print(f"{temp}C = {(temp*9/5)+32}F")
elif unidad == "Fahrenheit" or unidad == "farenheit":
    print(f"{temp}F = {(temp-32)*5/9}C")
else:
    print("Debes introducir una unidad valida")