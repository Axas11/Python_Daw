from Gafa import Gafa
class GafaGraduada(Gafa):
    def __init__(self, marca, modelo, fecha_lanzamiento, colores_disponibles, graduacion, tipo_cristal, tiene_filtro_luz_azul, precio, stock):
        super().__init__(marca, modelo, fecha_lanzamiento, colores_disponibles)
        self.graduacion = graduacion
        self.tipo_cristal = tipo_cristal
        self.tiene_filtro_luz_azul = tiene_filtro_luz_azul
        self.precio = precio
        self.stock = stock

    def __str__(self):
        base = super().__str__()
        filtro = "Si" if self.tiene_filtro_luz_azul else "No"
        return base + ", Graduacion: " + str(self.graduacion) + ", Tipo Cristal: " + self.tipo_cristal + ", Filtro Azul: " + filtro + ", Precio: " + str(self.precio) + "$, Stock: " + str(self.stock)

    def __lt__(self, other):
        return self.precio < other.precio

    def __le__(self, other):
        return self.precio <= other.precio

    def __gt__(self, other):
        return self.precio > other.precio

    def __ge__(self, other):
        return self.precio >= other.precio