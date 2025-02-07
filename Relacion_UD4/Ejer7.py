#Ejercicio 7. Crea una variable con tu nombre completo (nombre + apellidos) y muestra por pantalla, 
# en orden de aparición, las vocales que hay en tu nombre completo. 
nombre = "paco"
for letra in nombre:
    if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(letra)