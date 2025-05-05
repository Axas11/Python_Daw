from datetime import datetime
from GafaGraduada import GafaGraduada
from ColeccionGafas import ColeccionGafas

def parsear_fecha(texto):
    return datetime.strptime(texto, "%d/%m/%Y")

def colores_desde_texto(cadena):
    return [c.strip() for c in cadena.split(",")]

def crear_gafas_iniciales():
    return [
        GafaGraduada("Ray-Ban", "RB001", datetime(2022, 5, 1), ["negro", "azul"], 1.5, "monofocal", True, 120.0, 5),
        GafaGraduada("Oakley", "OX3218", datetime(2023, 3, 15), ["rojo"], 2.0, "progresivo", False, 180.0, 3),
        GafaGraduada("Vogue", "VG202", datetime(2021, 1, 10), ["dorado", "negro"], 0.75, "monofocal", True, 95.5, 4),
        GafaGraduada("Persol", "PO3007V", datetime(2022, 9, 5), ["marron"], 1.25, "bifocal", False, 210.0, 2),
        GafaGraduada("Guess", "GU1909", datetime(2023, 6, 25), ["azul", "verde"], 1.75, "progresivo", True, 160.0, 6),
        GafaGraduada("Hugo Boss", "HB1010", datetime(2022, 12, 1), ["negro"], 1.0, "monofocal", True, 130.0, 4),
        GafaGraduada("Tommy Hilfiger", "TH1675", datetime(2023, 4, 20), ["gris"], 2.25, "bifocal", False, 175.0, 5),
        GafaGraduada("Police", "PL999", datetime(2021, 11, 30), ["negro", "plata"], 0.5, "progresivo", True, 100.0, 7),
        GafaGraduada("Prada", "PR123", datetime(2022, 8, 8), ["azul"], 1.8, "monofocal", False, 220.0, 2),
        GafaGraduada("Fendi", "FE456", datetime(2023, 2, 17), ["transparente"], 1.6, "progresivo", True, 190.0, 3),
    ]

def mostrar_menu():
    print("\nColección de Gafas:")
    print(coleccion)
    print("\nSelecciona una opción:")
    print("Número → ver y modificar una gafa")
    print("Número negativo → eliminar una gafa")
    print("C → crear nueva gafa")
    print("O → ordenar por precio")
    print("B → buscar gafas por marca")
    print("F → filtrar gafas con filtro de luz azul")
    print("S → salir")

def editar_gafa(gafa):
    print("\nAtributos actuales:")
    print(coleccion.mostrar(gafas.index(gafa)))
    opciones = ["marca", "modelo", "fecha_lanzamiento", "colores_disponibles", "graduacion", "tipo_cristal", "tiene_filtro_luz_azul", "precio", "stock"]
    indice = int(input("Número del atributo a modificar: ")) - 1
    if indice == 2:
        nueva_fecha = input("Nueva fecha (dd/mm/aaaa): ")
        gafa.fecha_lanzamiento = parsear_fecha(nueva_fecha)
    elif indice == 3:
        nuevos_colores = input("Nuevos colores (separados por coma): ")
        gafa.colores_disponibles = colores_desde_texto(nuevos_colores)
    elif indice == 6:
        gafa.tiene_filtro_luz_azul = input("¿Tiene filtro azul (si/no)? ").lower() == "si"
    elif indice == 4 or indice == 7 or indice == 8:
        setattr(gafa, opciones[indice], float(input(f"Nuevo valor para {opciones[indice]}: ")))
    else:
        setattr(gafa, opciones[indice], input(f"Nuevo valor para {opciones[indice]}: "))

coleccion = ColeccionGafas()
gafas = crear_gafas_iniciales()
for g in gafas:
    coleccion.insertar(g)

while True:
    mostrar_menu()
    opcion = input("Opción: ").strip()

    if opcion.lower() == "s":
        break
    elif opcion.lower() == "c":
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        fecha = parsear_fecha(input("Fecha de lanzamiento (dd/mm/aaaa): "))
        colores = colores_desde_texto(input("Colores (separados por coma): "))
        graduacion = float(input("Graduacion: "))
        tipo = input("Tipo de cristal (monofocal/bifocal/progresivo): ").lower()
        filtro = input("¿Tiene filtro luz azul? (si/no): ").lower() == "si"
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        nueva = GafaGraduada(marca, modelo, fecha, colores, graduacion, tipo, filtro, precio, stock)
        coleccion.insertar(nueva)
    elif opcion.lower() == "o":
        orden = input("¿Orden ascendente o descendente? (a/d): ").lower()
        if orden == "d":
            coleccion.ordenar_por_precio_descendente()
        else:
            coleccion.ordenar_por_precio_ascendente()
        print("\nGafas ordenadas por precio:")
        print(coleccion)
    elif opcion.lower() == "b":
        marca = input("Marca a buscar: ")
        resultados = coleccion.buscar_por_marca(marca)
        if resultados:
            for elemento in enumerate(resultados):
                print(str(elemento[0] + 1) + ". " + str(elemento[1]))
        else:
            print("No se encontraron gafas con esa marca.")
    elif opcion.lower() == "f":
        filtradas = coleccion.filtrar_con_filtro_azul()
        if filtradas:
            for elemento in enumerate(filtradas):
                print(str(elemento[0] + 1) + ". " + str(elemento[1]))
        else:
            print("No hay gafas con filtro de luz azul.")
    elif opcion.startswith("-"):
        pos = int(opcion)
        if pos < 0:
            pos = -pos
            confirmar = input(f"¿Seguro que deseas borrar la gafa {pos}? (s/n): ").lower()
            if confirmar == "s":
                coleccion.borrar(pos)
    elif opcion.isdigit():
        pos = int(opcion)
        if pos < len(coleccion.gafas):
            g = coleccion.gafas[pos]
            editar_gafa(g)
        else:
            print("Esa posición no existe.")
    else:
        print("Opción no válida")