#Ejercicio 2. Crea una lista con el nombre de los planetas del sistema solar. Muestra por pantalla aquello que empiecen por la letra M.
planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno"]
for e in planetas:
    if e[0] == "M":
        print (e)