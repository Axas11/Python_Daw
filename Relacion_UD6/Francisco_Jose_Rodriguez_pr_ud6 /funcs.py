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
            else:
                print("Su usuario no se encuentra en la lista, intentalo de nuevo: ")

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
        intento += 1
