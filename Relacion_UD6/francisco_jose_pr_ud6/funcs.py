from Videojuego import Videojuego
from Usuario import Usuario
from datos import get_juegos, get_usuarios

def buscar_usuario(nombre_usuario, usuarios):
    for usuario in usuarios:
        if usuario.nombre == nombre_usuario:
            return usuario
    return None

def verificar_contra(contrasena, usuario):
    return usuario.contra == contrasena

def verificar_usuario():
    usuarios = get_usuarios()
    while True:
        nombre_usuario = input("Login: ")
        usuario = buscar_usuario(nombre_usuario, usuarios)
        if usuario:
            intentos = 3
            while intentos > 0:
                contrasena = input("Contrasena: ")
                if verificar_contra(contrasena, usuario):
                    print("Acceso concedido")
                    return usuario
                else:
                    intentos = intentos - 1
                    print(f"Contrasena incorrecta. Intentos restantes: {intentos}")
            print("Has agotado todos los intentos.")
            return None
        else:
            print("El nombre de usuario no existe.")

def mostrar_juegos(juegos):
    if juegos:
        for i, juego in enumerate(juegos, 1):
            print(f"[{i}]. {juego.nombre}, precio: {juego.precio_final(0.21, 0)}$")
    else:
        print("No hay juegos disponibles.")

def meter_dinero(usuario):
    while True:
        cantidad = float(input("Cantidad a ingresar: "))
        usuario.saldo = usuario.saldo + cantidad
        print(f"Has ingresado {cantidad}$. Saldo total: {usuario.saldo}$")

def gestionar_carrito(carrito, usuario, juegos_comprados):
    if not carrito:
        print("El carrito esta vacio.")
        return
    
    total = sum(juego.precio_final(0.21, 0) for juego in carrito)
    print("CARRITO DE COMPRA")
    mostrar_juegos(carrito)
    print(f"Total a pagar: {total}$")
    
    if usuario.saldo >= total:
        confirmar = input("¿Quieres comprar estos juegos? (S/n): ")
        if confirmar == "s":
            for juego in carrito:
                juegos_comprados.append(juego)
                usuario.saldo = usuario.saldo - juego.precio_final(0.21, 0)
            carrito.clear()
            print("Compra realizada.")
        else:
            print("Compra cancelada.")
    else:
        print("Saldo insuficiente.")

def filtro_edad(juegos, usuario):
    return [juego for juego in juegos if usuario.edad() >= juego.PEGI]

def print_menu(juegos_aptos, usuario):
    print("JUEGOS DISPONIBLES PARA COMPRAR: ")
    for i, juego in enumerate(juegos_aptos, 1):
        print(f"[{i}]. {juego.nombre}, precio: {juego.precio_final(0.21, 0)}$")
    print("-------------------------------------")
    print(f"Actualmente tiene: {usuario.saldo:.2f}$")
    print("-------------------------------------")
    print("[V]er mis juegos")
    print("[I]ngresar dinero")
    print("Ir al [c]arrito")
    print("[S]alir")

def menu():
    usuario = verificar_usuario()    
    if not usuario:
        return
    
    juegos = get_juegos()
    juegos_aptos = filtro_edad(juegos, usuario)
    carro = []
    juegos_comprados = []
    precio_total = 0
    
    while True:
        print_menu(juegos_aptos, usuario)
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "s":
            print("Gracias por usar la tienda.")
            break
        
        match opcion:
            case "c":
                if len(carro) >= 1: 
                    print("Juegos en el carrito")
                    precio_total = 0
                    for juego in carro:
                        precio_actual = juego.precio_final(0.21, 0)
                        print(f"{juego.nombre}, precio: {precio_actual}$")
                        precio_total = precio_total + precio_actual
                    
                    print(f"El precio total es: {precio_total}$")
                    
                    pagar = input("Quieres comprar estos juegos? (S/n): ")
                    if pagar == "S" and usuario.saldo >= precio_total:
                        print("Gracias por su compra")
                        for juego in carro:
                            juegos_comprados.append(juego)
                        carro.clear()
                        usuario.saldo = usuario.saldo - precio_total
                        input()
                    elif pagar == "S" and usuario.saldo < precio_total:
                        print("No tienes suficiente dinero") 
                        input() 
                else:
                    print("No tienes ningun juego en el carro")
                    input()
            
            case "v":
                if len(juegos_comprados) >= 1:
                    print("Juegos: ")
                    for juego in juegos_comprados:
                        print(juego.nombre)
                    input()
                else: 
                    print("No tienes juegos comprados")
                    input()
            
            case "i":
                while True:
                    ingreso = float(input("Cantidad a ingresar: "))
                    if ingreso > 0:
                        usuario.saldo = usuario.saldo + ingreso
                        print(f"Enhorabuena has ingresado: {ingreso:.2f}$")
                        input()
                        break
                    else:
                        print("Vuelva a introducir la cantidad ")

            case _:
                if opcion.isdigit():
                    opcion = int(opcion)
                    
                    if 0 < opcion <= len(juegos_aptos):
                        juego_seleccionado = juegos_aptos[opcion-1]
                        print(f"{juego_seleccionado}")
                        mandar_carro = input("Quieres llevar este juego al carrito? (S/n): ")
                        
                        if mandar_carro == "S":
                            juegos_aptos.remove(juego_seleccionado)
                            carro.append(juego_seleccionado)
                            print("Juego añadido al carrito")
                            input()
                    else:
                        print("No existe esa opcion")
                        input()
                else:
                    print("No existe esa opcion")
                    input()
