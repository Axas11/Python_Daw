from libro import libro
libros = [
    libro("Crimen y castigo", ["Fiódor Dostoievski"], 671, ["Novela", "Filosofía", "Psicológica"], 10),
    libro("Guerra y paz", ["León Tolstói"], 1225, ["Novela", "Histórica"], 10),
    libro("Anna Karénina", ["León Tolstói"], 864, ["Novela", "Drama", "Romance"], 9),
    libro("El maestro y Margarita", ["Mijaíl Bulgákov"], 384, ["Fantasía", "Satírica"], 9),
    libro("Los hermanos Karamázov", ["Fiódor Dostoievski"], 1013, ["Novela", "Filosofía", "Drama"], 10),
    libro("1984", ["George Orwell"], 328, ["Distopía", "Ciencia ficción"], 10),
    libro("Cien años de soledad", ["Gabriel García Márquez"], 471, ["Realismo mágico", "Drama"], 10),
    libro("Ulises", ["James Joyce"], 730, ["Experimental", "Filosofía"], 8),
    libro("Moby-Dick", ["Herman Melville"], 635, ["Aventura", "Clásico"], 9),
    libro("Don Quijote de la Mancha", ["Miguel de Cervantes"], 863, ["Aventura", "Clásico", "Sátira"], 10)
]
libros_espanoles = [
    libro("Don Quijote de la Mancha", ["Miguel de Cervantes"], 863, ["Aventura", "Clásico", "Sátira"], 10),
    libro("La Regenta", ["Leopoldo Alas"], 928, ["Novela", "Realismo", "Drama"], 9),
    libro("Fortunata y Jacinta", ["Benito Pérez Galdós"], 1056, ["Novela", "Costumbrismo", "Drama"], 9),
    libro("Campos de Castilla", ["Antonio Machado"], 208, ["Poesía", "Reflexión"], 9),
    libro("Platero y yo", ["Juan Ramón Jiménez"], 138, ["Narrativa", "Poesía en prosa"], 8),
    libro("Bodas de sangre", ["Federico García Lorca"], 128, ["Teatro", "Tragedia", "Poesía"], 9),
    libro("La colmena", ["Camilo José Cela"], 304, ["Novela", "Costumbrismo"], 8),
    libro("Nada", ["Carmen Laforet"], 288, ["Novela", "Existencialismo"], 9),
    libro("El camino", ["Miguel Delibes"], 176, ["Novela", "Realismo"], 8),
    libro("Los santos inocentes", ["Miguel Delibes"], 254, ["Novela", "Drama social"], 9)
]
#EJ 10.1
print("###Encontrar los libros escritos por Dostoievski con más de 1000 páginas###")
libros_filtrados = [libro for libro in libros if "Fiódor Dostoievski" in libro.autores and libro.paginas > 1000]
for libro in libros_filtrados:
    print(libro)
#EJ 10.2
print("###Encontrar los libros con menos de 400 páginas###")
libros_filtrados2 = [libro for libro in libros if libro.paginas < 400]
for libro in libros_filtrados2:
    print(libro)
#EJ 10.3
print("###Encontrar los libros cuyo nombre es un número###")
libros_filtrados3 = [libro for libro in libros if libro.nombre.isnumeric()]
for libro in libros_filtrados3:
    print(libro)
#EJ 10.4
print("###Encontrar (sin repetir) los escritores de la lista###")
sin_repetir = []
for libro in libros:
    if libro.autores not in sin_repetir:
        sin_repetir.append(libro.autores)
        print(libro.autores)
#EJ 11.1
print("###Encontrar los mejores libros de la historia que además son españoles###")
mejores_espanoles = []
for libro_mejor in libros:
    for libro_espanol in libros_espanoles:
        if libro_mejor.nombre == libro_espanol.nombre:
            mejores_espanoles.append(libro_mejor)

for libro in mejores_espanoles:
    print(libro.nombre)

#EJ 11.2
print("###Encontrar los mejores escritores españoles cuyos libros NO estén dentro de los mejores libros escritos por la humanidad###")

mejores_espanoles = []
libro_todos = [libro.nombre for libro in libros]
for libro in libros_espanoles:
    if libro.nombre not in libro_todos:
        mejores_espanoles.append(libro)

sin_repetir = []
for libro in mejores_espanoles:
    if libro.autores not in sin_repetir:
          sin_repetir.append(libro.autores)
          print(libro.autores)

#EJ 11.3
print("###Encontrar los mejores libros (españoles o mundiales) que empiezan por D (no puede haber repeticiones)###")
empiezan_por_d = []
for libro in libros:
      if libro.nombre[0] == "D":
            empiezan_por_d.append(libro.nombre)

for libro in libros_espanoles:
      if libro.nombre[0] == "D" and libro.nombre not in empiezan_por_d:
            empiezan_por_d.append(libro.nombre)

print(empiezan_por_d)

#EJ 11.4
print("###¿Quién es el mejor escritor español? (Calcular el mejor escritor español como aquel que que más títulos tiene en la lista de mejores libros españoles)###")
apariciones = 0
mejor_escritor = None
mejores_escritores = []

for libro in libros_espanoles:
    for autor in libro.autores:
        mejores_escritores.append(autor)

for escritor in mejores_escritores:
    contador = 0
    for libro in libros_espanoles:
        if escritor in libro.autores:
            contador = contador + 1
    if contador > apariciones:
        apariciones = contador
        mejor_escritor = escritor

print(escritor)
        




