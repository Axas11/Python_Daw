#Crea una lista con palabras. Crea una segunda lista que contenga las mismas palabras pero con todas sus letras en mayúscula.

palabras = ["hola", "dios", "casa", "perro", "gato", "avion", "arbol", "azul", "amarillo", "rojo", "verde", "naranja", "blanco"]

palabras_mayus = [palabra.upper() for palabra in palabras]
print(f"Lista de palabras: {palabras}")
print(f"Lista de palabras en mayúsculas: {palabras_mayus}")