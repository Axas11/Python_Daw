from Videojuego import Videojuego
from Usuario import Usuario
from datos import get_juegos, get_usuarios
from datetime import datetime
from funcs import (
    login,
    juegos_disponibles,
    juegos_disponibles_user,
    menu_tienda,
)


usuarios = get_usuarios()
juegos = get_juegos()
usuario = login()
menu = menu_tienda()

    





