class ColeccionGafas:
    def __init__(self, coleccion):
        self.gafas = coleccion

    def __str__(self):
        resultado = ""
        for i, gafa in enumerate(self.gafas):
            linea = str(i) + ". " + gafa.marca + " - " + gafa.modelo + " (" + str(gafa.precio) + "$)\n"
            resultado += linea
        return resultado.strip()

    def insertar(self, gafa):
        self.gafas.append(gafa)

    def borrar(self, pos):
        if 0 <= pos < len(self.gafas):
            del self.gafas[pos]
        else:
            print("Posicion no valida. No se pudo borrar.")

    def mostrar(self, pos):
        if 0 <= pos < len(self.gafas):
            gafa = self.gafas[pos]
            atributos = [
                "1. Marca: " + gafa.marca,
                "2. Modelo: " + gafa.modelo,
                "3. Fecha Lanzamiento: " + gafa.fecha_lanzamiento.strftime("%d/%m/%Y"),
                "4. Colores: " + ", ".join(gafa.colores_disponibles),
                "5. Graduacion: " + str(gafa.graduacion),
                "6. Tipo Cristal: " + gafa.tipo_cristal,
                "7. Filtro Luz Azul: " + ("Si" if gafa.tiene_filtro_luz_azul else "No"),
                "8. Precio: " + str(gafa.precio) + "$",
                "9. Stock: " + str(gafa.stock)
            ]
            return "\n".join(atributos)
        else:
            print("Posicion no valida.")

    def buscar_por_marca(self, marca):
        return [g for g in self.gafas if g.marca.lower() == marca.lower()]

    def filtrar_con_filtro_azul(self):
        return [g for g in self.gafas if g.tiene_filtro_luz_azul]
