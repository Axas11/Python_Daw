
import math

def areaTriangulo(base: float, altura: float) -> float:
    """Calcula el área de un triángulo

    :base: número real mayor a 0
    :altura: número real mayor a 0

    :raises ValueError: si base o altura <= 0

    :return: el área del triángulo cuya base y altura son las pasadas como parámetros
    """
    if base <= 0 or altura <= 0:
        raise ValueError("Tanto base como altura deben ser un número positivo")
    area = base * altura / 2
    return area

def areaRectangulo(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo

    :base: número real mayor a 0
    :altura: número real mayor a 0

    :raises ValueError: si base o altura <= 0

    :return: el área del rectángulo cuya base y altura son las pasadas como parámetros
    """
    if base <= 0 or altura <= 0:
        raise ValueError("Tanto base como altura deben ser un número positivo")
    area = base * altura
    return area

def areaCirculo(radio: float) -> float:
    """Calcula el área de un círculo

    :radio: número real mayor a 0

    :raises ValueError: si radio <= 0

    :return: el área del círculo con el radio pasado como parámetro
    """
    if radio <= 0:
        raise ValueError("El radio debe ser un número positivo")
    area = math.pi * radio * radio
    return area
