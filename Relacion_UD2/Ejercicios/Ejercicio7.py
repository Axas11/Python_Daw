curso = input("En que curso estas matriculado")
ano = int(input("En que ano estas matriculado"))
if curso == "DAW" and ano == 1 or curso == "DAM" and ano == 1:
    print("Tienes que cursar programacion")
else:
    print("No tienes que cursar programacion")