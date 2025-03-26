from funcs import login, juegos_disponibles, juegos_disponibles_user, meter_dinero, carrito
from datos import get_usuarios, get_juegos
from Usuario import Usuario
from Videojuego import Videojuego

usuario = None
juegos_comprados = []
carrito_actual = []

while True:
    print("\n--- Menú ---")
    print("1. Iniciar sesión")
    print("2. Ver juegos disponibles")
    print("3. Añadir dinero")
    print("4. Ver carrito")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        usuario = login()
        if usuario is None:
            print("No se pudo iniciar sesión. Inténtalo de nuevo.")
    
    elif opcion == "2":
        if usuario is None:
            print("Debes iniciar sesión primero.")
        else:
            juegos_filtrados = juegos_disponibles(usuario)
            juegos_disponibles_user(juegos_filtrados)
            juego_numero = int(input("Selecciona un juego para añadir al carrito (por número): "))
            if 1 <= juego_numero <= len(juegos_filtrados):
                juego = juegos_filtrados[juego_numero - 1]
                usuario, juegos_comprados = carrito(carrito_actual, usuario, juegos_comprados, juego)
                carrito_actual.append(juego)  # Añadimos el juego al carrito
            else:
                print("Selección inválida.")
    
    elif opcion == "3":
        if usuario is None:
            print("Debes iniciar sesión primero.")
        else:
            usuario = meter_dinero(usuario)
    
    elif opcion == "4":
        if usuario is None:
            print("Debes iniciar sesión primero.")
        else:
            print("\nJuegos en tu biblioteca:")
            for i, juego in enumerate(juegos_comprados, 1):
                print(f"{i}. {juego}")
    
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción correcta.")