from Videojuego import Videojuego
from Usuario import Usuario
from datos import get_juegos, get_usuarios
from datetime import datetime
import funcs

#funcs.login_usuario(nombre_usuario)
from funcs import login
usuario = login()

if usuario:
    print(f"¡Bienvenido, {usuario.nombre}!")
else:
    print("Acceso denegado. Inténtalo más tarde.")