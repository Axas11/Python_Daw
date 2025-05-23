from datetime import datetime
from GafaGraduada import GafaGraduada
from ColeccionGafas import ColeccionGafas

def mostrar_menu():
    print("\nColeccion de Gafas:")
    print(coleccion)
    print("\nSelecciona una opcion:")
    print("Numero -> ver y modificar una gafa")
    print("Numero negativo -> eliminar una gafa")
    print("C -> crear nueva gafa")
    print("O -> ordenar por precio")
    print("B -> buscar gafas por marca")
    print("F -> filtrar gafas con filtro de luz azul")
    print("S -> salir")

def editar_gafa(gafa):
    print("\nAtributos actuales:")
    print(coleccion.mostrar(gafas.index(gafa)))
    indice = int(input("Numero del atributo a modificar: ")) - 1

    if indice == 0:
        gafa.marca = input("Nuevo valor para marca: ")
    elif indice == 1:
        gafa.modelo = input("Nuevo valor para modelo: ")
    elif indice == 2:
        nueva_fecha = input("Nueva fecha (dd/mm/aaaa): ")
        gafa.fecha_lanzamiento = datetime.strptime(nueva_fecha, "%d/%m/%Y")
    elif indice == 3:
        nuevos_colores = input("Nuevos colores: ")
        gafa.colores_disponibles = [c.strip() for c in nuevos_colores.split(",")]
    elif indice == 4:
        gafa.graduacion = float(input("Nuevo valor para graduacion: "))
    elif indice == 5:
        gafa.tipo_cristal = input("Nuevo valor para tipo_cristal: ")
    elif indice == 6:
        gafa.tiene_filtro_luz_azul = input("Tiene filtro azul (si/no)? ").lower() == "si"
    elif indice == 7:
        gafa.precio = float(input("Nuevo valor para precio: "))
    elif indice == 8:
        gafa.stock = int(input("Nuevo valor para stock: "))

gafas = [
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

coleccion = ColeccionGafas(gafas)

while True:
    mostrar_menu()
    opcion = input("Opcion: ").strip()

    if opcion.lower() == "s":
        break
    elif opcion.lower() == "c":
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        fecha = datetime.strptime(input("Fecha de lanzamiento (dd/mm/aaaa): "), "%d/%m/%Y")
        colores = [c.strip() for c in input("Colores (separados por coma): ").split(",")]
        graduacion = float(input("Graduacion: "))
        tipo = input("Tipo de cristal (monofocal/bifocal/progresivo): ").lower()
        filtro = input("Tiene filtro luz azul? (si/no): ").lower() == "si"
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        nueva = GafaGraduada(marca, modelo, fecha, colores, graduacion, tipo, filtro, precio, stock)
        coleccion.insertar(nueva)
    elif opcion.lower() == "o":
        orden = input("Orden ascendente o descendente? (a/d): ").lower()
        if orden == "d":
            coleccion.gafas.sort()
            coleccion.gafas.reverse()
        else:
            coleccion.gafas.sort()
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
        confirmar = input("Seguro que deseas borrar la gafa " + str(pos) + "? (s/n): ").lower()
        if confirmar == "s":
            coleccion.borrar(pos*-1)
    elif opcion.isdigit():
        pos = int(opcion)
        if pos < len(coleccion.gafas):
            g = coleccion.gafas[pos]
            editar_gafa(g)
        else:
            print("Esa posicion no existe.")
    else:
        print("Opcion no valida")
