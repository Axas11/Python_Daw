curso = input("En que curso estas matriculado")
ano = int(input("En que ano estas matriculado"))
if curso == "ASIR" and ano == 1 or curso == "DAW" and ano == 2:
    print("Este ano vas a aprender a desplegar redes")
else:
    print("Este ano no vas a aprender a desplegar redes")