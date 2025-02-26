# Convierte una cadena en lista y calcula la longitud de cada palabra
frase = "Python es un lenguaje de programación"
palabras = frase.split()
longitudes = [len(p) for p in palabras]
print(longitudes)