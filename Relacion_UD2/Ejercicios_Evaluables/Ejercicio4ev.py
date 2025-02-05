def convertir_unidades_masa(cantidad, udini, udfin):
    cantconv = 0

    if udini == "gramos" and udfin == "kilos":
        cantconv = cantidad / 1000
    elif udini == "gramos" and udfin == "toneladas":
        cantconv = cantidad / 1000000
    elif udini == "kilos" and udfin == "gramos":
        cantconv = cantidad * 1000
    elif udini == "kilos" and udfin == "toneladas":
        cantconv = cantidad / 1000
    elif udini == "toneladas" and udfin == "gramos":
        cantconv = cantidad * 1000000
    elif udini == "toneladas" and udfin == "kilos":
        cantconv = cantidad * 1000

    print(f"{cantidad} {udini} son {cantconv} {udfin}")

    return cantconv
cantidad = float(input("Introduce la cantidad : "))
udini = input("Introduce la unidad inicial (gramos, kilos o toneladas): ")
udfin = input("Introduce la unidad final (gramos, kilos o toneladas): ")
resultado = convertir_unidades_masa(cantidad, udini, udfin)