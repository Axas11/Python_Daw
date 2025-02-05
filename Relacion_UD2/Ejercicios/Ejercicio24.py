user = input("Introduce su usuario: ")
pass1 = input("Introduce tu pass: ")
pass2 = input("Introduce tu pass de nuevo: ")
while pass1 != pass2:
    print("Las pass no coinciden")
    pass1 = input("Introduce tu pass: ")
    pass2 = input("Introduce tu pass de nuevo: ")
print(f"Has creado satisfactoriamente tu cuenta: user: {user} pass: {pass2} ")