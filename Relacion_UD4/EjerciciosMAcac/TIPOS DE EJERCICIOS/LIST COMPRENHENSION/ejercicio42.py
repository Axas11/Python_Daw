#Ejercicio 42. Crea una lista con palabras. Crea una segunda lista que contenga sólo las palabras que empiezan por a.

palabras = ["hola", "dios", "casa", "perro", "gato", "avion", "arbol", "azul", "amarillo", "rojo", "verde", "naranja", "blanco"]

palabras_a = [palabra for palabra in palabras if palabra.lower()[0] == "a"]

print(f"Lista de las palabras: {palabras}")
print(f"Lista de palabras que solo empiezan por la a: {palabras_a}")

