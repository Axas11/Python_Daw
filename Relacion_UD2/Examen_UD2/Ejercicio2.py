def kilosalibra(num1):
    libra = 0.453592
    conversion = (num1/libra)
    print(f"{num1} kilogramos son {conversion} libras")  

resultado = float(input("Inserta un peso en kilogramos: "))

kilosalibra(resultado)