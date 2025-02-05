from funcs import menu, cuentaRandom, configuracion, logros, estadisticas
vidas = 3
vidasConf = 3
numJugadas = 0
operacionTotal = 0
aciertosTotal = 0
fallosTotal = 0
numMin = 0
numMax = 10
acierto = 0
fallo = 0
racha = 0
rachaMax = 0
bronce = False
plata = False
oro = False
platino = False

while True:
    fallo = 0
    acierto = 0
    vidas = vidasConf
    menu()
    opcionMenu=(input("Opcion: "))
    match opcionMenu:
        case "1":
            while vidas > 0:
                if racha>rachaMax:
                    rachaMax = racha
                operacionTotal = operacionTotal + 1
                resultado=cuentaRandom(numMin, numMax)
                respuesta=int(input("Respuesta: "))
                if respuesta == resultado:
                    print("Acertaste!")
                    racha = racha + 1
                    acierto = acierto + 1
                    aciertosTotal = aciertosTotal + 1
                else:
                    print(f"Fallaste, el resultado era {resultado}")
                    racha = 0
                    fallo = fallo + 1
                    fallosTotal = fallosTotal + 1
                    vidas = vidas - 1
                    print(f"Vidas restantes: {vidas} ")
                if racha == 3 and bronce == False:
                    bronce = True
                    print("CONSEGUIDO!!: bronce")
                if racha == 7 and plata == False:
                    plata =True
                    print("CONSEGUIDO!!: plata")
                if racha == 10 and oro == False:
                    oro = True
                    print("CONSEGUIDO!!: oro")
                if numMin > 10 and numMax > 15 and racha == 10:
                    platino = True
                    print("CONSEGUIDO!!: platino")


            numJugadas = numJugadas + 1
            print(f"En tu partida numero {numJugadas} acertaste {acierto} operaciones y has fallado {fallo}")
            print(f"Acertaste un porcentaje {round(acierto * 100 / operacionTotal, 2)}% de las cuentas")

        case "2":
            while True:
                configuracion(vidasConf, numMin, numMax)

                seleccionMenu = (input("Que deseas hacer?"))
                match seleccionMenu:
                    case "1":
                        vidasConf = int(input("Entre 1 y 10:"))
                        while vidasConf < 0 or vidasConf > 10:
                            vidasConf = int(input("Entre 1 y 10: "))

                    case "2":
                        numMin = int(input("Nuevo minimo"))
                        while numMin>numMax:
                            numMin = int(input("NumMin tiene que ser menor que NumMax"))
                    case "3":
                        numMax = int(input("Nuevo maximo"))
                        while numMax < numMin:
                            numMax = int(input("NumMax tiene que ser mayor que NumMin"))
                    case "0":
                        break

        case "3":
            estadisticas(numJugadas, operacionTotal, aciertosTotal, fallosTotal, rachaMax)

        case "4":
            logros(bronce, plata, oro, platino)

        case "0":
            break