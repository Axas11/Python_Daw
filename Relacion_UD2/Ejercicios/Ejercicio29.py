user = input("Inserta tu usuario: ")
pass1 = str(input("Introduce tu contrasena: "))
while True:
    pass2 = str(input("Introduce tu contrasena de nuevo: "))
    if pass1 == pass2:
        break
    else:
        input("Las contrasenas no coinciden")
print(f"Su usuario es {user} y su contrasena es {pass2}")

