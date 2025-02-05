def calcular_precio(dia, tipo, festivo, cupon):
    precio_base = 0
    
    if dia == "lunes" or dia == "martes" or dia == "miercoles" or dia == "jueves":
        if tipo == "individual":
            precio_base = 30
        else:
            precio_base = 50
    elif dia == "viernes" or dia == "sabado":
        if tipo == "individual":
            precio_base = 45
        else:
            precio_base = 70
    else:
        if tipo == "individual":
            precio_base = 40
        else:
            precio_base = 60

    if festivo == "si":
        precio_base *= 1.1 
    else:
        if cupon:
            precio_base *= 0.9  

    return precio_base

dia = input("Dia (lunes, martes, etc.): ")
tipo = input("Habitacion(individual, doble): ")
festivo = input("¿Es festivo? (sí/no): ")
cupon = input("¿Tiene cupón de descuento? (sí/no): ").lower() == "sí"

precio = calcular_precio(dia, tipo, festivo, cupon)
print("El precio de la habitación es:", precio, "€")