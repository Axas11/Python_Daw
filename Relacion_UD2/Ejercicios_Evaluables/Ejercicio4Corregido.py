def convertirpesos(cantidad: float, unidad1: str, unidad2:str) -> float:
    resultado = cantidad
    if unidad1 == "gr":
        if unidad2 == "kg":
            resultado /= 1000
        elif unidad2 == "t":
            resultado /= 1000000
    elif unidad1 == "kg":
        if unidad2 == "gr":
            resultado *=1000
        elif unidad2 == "t":
            resultado /= 1000
    elif unidad1 == "t":
        if unidad2 == "gr":
            resultado *= 10000000
        elif unidad2 == "kg":
            resultado *= 1000
        
    return resultado

        

        