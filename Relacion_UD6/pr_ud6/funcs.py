from Videojuego import Videojuego
from Usuario import Usuario
from datos import get_juegos, get_usuarios
from datetime import datetime

def login():
    usuarios = get_usuarios()
    usuario = None
    
    while usuario is None:
        nombre_usuario = input("Login: ")
        for user in usuarios:
            if user.nombre == nombre_usuario:
                usuario = user
                break
        if usuario is None:
            print("El usuario no se encuentra en la lista, intente de nuevo.")

    intento = 1
    max_intento = 3
    
    while intento <= max_intento:
        contrasena = input("Contraseña: ")
        
        if usuario.contra == contrasena:
            print("¡Acceso concedido!")
            return usuario
        
        if intento == max_intento:
            print("Has agotado tus intentos, vuelve a intentarlo más tarde.")
            return None
        
        print(f"Contraseña incorrecta. Intento {intento} de {max_intento}.")
        intento = intento + 1

def juegos_disponibles(usuario):
    juegos = get_juegos()
    edad_usuario = usuario.edad()
    juegos_filtrados = []

    for juego in juegos:
        if juego.PEGI <= edad_usuario:
            juegos_filtrados.append(juego)

    return juegos_filtrados

def juegos_disponibles_user(juegos_filtrados):
    for i, juego in enumerate(juegos_filtrados, 1):
        precio_final = juego.precio_final(0.21, 0)
        print(f"[{i}]. {juego.nombre}, precio: {precio_final}")

def mostrar_juegos(juegos_comprados):
    if not juegos_comprados:
        print("\nNo tienes juegos comprados.")
        return
    
    print("\nTUS JUEGOS:")
    for i, juego in enumerate(juegos_comprados, 1):
        print(f"{i}. {juego.nombre}")    

def meter_dinero(usuario):
    print("Cuanto dinero quieres ingresar?: ")
    cantidad = float(input())
    if cantidad <= 0:
        print("No puedes meter 0 euros")
        return usuario
    
    usuario.saldo = usuario.saldo + cantidad
    print(f"Ya has ingresado {cantidad} Tienes en total: {usuario.saldo}$")

    return usuario

def carrito(carrito, usuario, juegos_comprados, juego):
    if juego not in carrito:
        carrito.append(juego)
        print(f"{juego.nombre} añadido al carrito")
    else:
        print("Este juego ya lo has añadido al carrito")

    total = sum(juego.precio_final(0.21, 0) for juego in carrito if juego not in juegos_comprados)

    print("CARRITO DE COMPRA")
    for i, juego in enumerate(carrito, 1): ##revisar
        precio = juego.precio_final(0.21, 0)
        print(f"{i}. {juego} -> {precio}$")

    print(f"Total: {total}$")

    if total > usuario.saldo:
        print("No tienes suficiente saldo para completar la compra.")
        return usuario, juegos_comprados

    for juego in carrito:
        if juego not in juegos_comprados:
            juegos_comprados.append(juego)
            usuario.saldo -= juego.precio_final(0.21, 0)  

    print(f"Compra completada. Te quedan {usuario.saldo}$ en tu cuenta.")
    return usuario, juegos_comprados







    







