# Ejercicio 6
# Crea la dataclass Pelicula, con los siguientes atributos: titulo (str), es_animada (bool) y num_premios (int).
# Crea una lista con 9 objetos de la clase.
# Muestra por pantalla todos los objetos de la lista mostrando todos sus atributos.
# Filtra la lista para que contenga las peliculas animadas sin premios. Muestra por pantalla su titulo.
@dataclass
class Pelicula:
    titulo: str
    es_animada: bool
    num_premios: int

peliculas = [
    Pelicula("Toy Story", True, 3),
    Pelicula("El viaje de Chihiro", True, 5),
    Pelicula("Inside Out", True, 0),
    Pelicula("Titanic", False, 11),
    Pelicula("Avatar", False, 3),
    Pelicula("Soul", True, 0),
    Pelicula("Amelie", False, 2),
    Pelicula("Shrek", True, 1),
    Pelicula("Coco", True, 2)
]

for p in peliculas:
    print(p)

animadas_sin_premios = [p.titulo for p in peliculas if p.es_animada and p.num_premios == 0]
print("Peliculas animadas sin premios:", animadas_sin_premios)

# Ejercicio 7
# Crea la clase Pelicula con los atributos: titulo (str), fecha_estreno (datetime), valoracion (float), generos (list[str]).
# En el constructor, comprueba que la valoracion esté entre 0 y 10.
# Implementa los métodos: __eq__, __str__, __gt__, __ge__, __le__, __lt__, es_del_genero(genero: str) -> bool
class Pelicula:
    def __init__(self, titulo: str, fecha_estreno: datetime, valoracion: float, generos: list[str]):
        self.titulo = titulo
        self.fecha_estreno = fecha_estreno
        self.valoracion = max(0, min(10, valoracion))
        self.generos = generos

    def __eq__(self, other):
        return self.titulo == other.titulo and self.fecha_estreno == other.fecha_estreno

    def __str__(self):
        return f"{self.titulo} ({self.fecha_estreno.strftime('%Y-%m-%d')}), Valoracion: {self.valoracion}, Generos: {self.generos}"

    def __gt__(self, other): return self.valoracion > other.valoracion
    def __ge__(self, other): return self.valoracion >= other.valoracion
    def __le__(self, other): return self.valoracion <= other.valoracion
    def __lt__(self, other): return self.valoracion < other.valoracion

    def es_del_genero(self, genero: str) -> bool:
        return genero in self.generos

# Ejercicio 8
# Crea la clase EjemplarPelicula que herede de Pelicula.
# Añade los atributos: id (int), estado (int entre 1 y 5).
# Implementa los métodos: __eq__, __str__, __gt__, __ge__, __le__, __lt__, estado_str() -> str
class EjemplarPelicula(Pelicula):
    def __init__(self, id: int, estado: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.estado = max(1, min(5, estado))

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f"ID: {self.id}, {super().__str__()}, Estado: {self.estado_str()}"

    def __gt__(self, other): return self.estado < other.estado
    def __ge__(self, other): return self.estado <= other.estado
    def __le__(self, other): return self.estado >= other.estado
    def __lt__(self, other): return self.estado > other.estado

    def estado_str(self):
        estados = ["", "precintado", "como nuevo", "ligeros desperfectos", "desperfectos grandes", "sin caja y/o caratula"]
        return estados[self.estado]

# Ejercicio 9
# Crea la clase ColeccionPeliculas con una lista de ejemplares.
# Implementa los métodos: __str__, peliculas_repetidas(), mostrar_peliculas_repetidas(), eliminar_pelicula(id: int)
class ColeccionPeliculas:
    def __init__(self):
        self.ejemplares = []

    def __str__(self):
        return "\n".join([f"{e.titulo} - {e.estado_str()}" for e in self.ejemplares])

    def peliculas_repetidas(self):
        titulos = {}
        for e in self.ejemplares:
            key = (e.titulo, e.fecha_estreno)
            titulos[key] = titulos.get(key, 0) + 1
        return [Pelicula(t[0], t[1], 0, []) for t, count in titulos.items() if count > 1]

    def mostrar_peliculas_repetidas(self):
        for peli in self.peliculas_repetidas():
            print(peli.titulo)

    def eliminar_pelicula(self, id: int):
        self.ejemplares = [e for e in self.ejemplares if e.id != id]

    # Ejercicio 11
    # Añade los siguientes métodos: media_valoracion(), peliculas_por_genero(), mejor_valorada()
    def media_valoracion(self):
        if not self.ejemplares:
            return 0
        return sum(e.valoracion for e in self.ejemplares) / len(self.ejemplares)

    def peliculas_por_genero(self):
        resultado = {}
        for e in self.ejemplares:
            for genero in e.generos:
                if genero not in resultado:
                    resultado[genero] = set()
                resultado[genero].add(e.titulo)
        return {g: list(titulos) for g, titulos in resultado.items()}

    def mejor_valorada(self):
        if not self.ejemplares:
            return None
        return max(self.ejemplares, key=lambda e: (e.valoracion, e.fecha_estreno))

# Ejercicio 10
# Utilizando las clases anteriores, crea una coleccion de peliculas con varios ejemplares.
# Muestra todos los juegos, los repetidos, elimina uno por id, vuelve a mostrar repetidos.
coleccion = ColeccionPeliculas()
coleccion.ejemplares = [
    EjemplarPelicula(1, 2, "Matrix", datetime(1999, 3, 31), 9.0, ["accion", "ciencia ficcion"]),
    EjemplarPelicula(2, 3, "Matrix", datetime(1999, 3, 31), 9.0, ["accion", "ciencia ficcion"]),
    EjemplarPelicula(3, 1, "La La Land", datetime(2016, 12, 9), 8.5, ["musical", "romance"]),
    EjemplarPelicula(4, 5, "Origen", datetime(2010, 7, 16), 8.8, ["accion", "suspense"]),
    EjemplarPelicula(5, 2, "Origen", datetime(2010, 7, 16), 8.8, ["accion", "suspense"])
]

print("--- Coleccion de Peliculas ---")
print(coleccion)
print("--- Peliculas Repetidas ---")
coleccion.mostrar_peliculas_repetidas()

coleccion.eliminar_pelicula(4)
print("--- Peliculas Repetidas Tras Eliminar ID 4 ---")
coleccion.mostrar_peliculas_repetidas()

# Ejercicio 11 - Estadísticas
# Añade funciones de análisis a la coleccion: media_valoracion, peliculas_por_genero, mejor_valorada
print("--- Media de Valoracion ---")
print(coleccion.media_valoracion())

print("--- Peliculas por Genero ---")
for genero, titulos in coleccion.peliculas_por_genero().items():
    print(f"{genero}: {titulos}")

print("--- Mejor Valorada ---")
print(coleccion.mejor_valorada())

# Ejercicio 12
# Crea una funcion que busque ejemplares compatibles por genero y estado minimo
# buscar_ejemplares_compatibles(coleccion, genero: str, minimo_estado: int)
def buscar_ejemplares_compatibles(coleccion: ColeccionPeliculas, genero: str, minimo_estado: int):
    return [e for e in coleccion.ejemplares if genero in e.generos and e.estado <= minimo_estado]

print("--- Ejemplares compatibles (genero='accion', estado<=2) ---")
for ejemplar in buscar_ejemplares_compatibles(coleccion, "accion", 2):
    print(ejemplar)