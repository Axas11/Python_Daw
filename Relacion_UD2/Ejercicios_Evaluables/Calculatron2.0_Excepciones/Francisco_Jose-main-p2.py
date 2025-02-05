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
    try:
        opcionMenu = input("Opcion: ")
    except ValueError:
        print("Error: Debes introducir un número valido.")
    except Exception as error:
        print(f"Se ha producido un error: {error}")
    
    match opcionMenu:
        case "1":
            while vidas > 0:
                try:
                    if racha > rachaMax:
                        rachaMax = racha
                    operacionTotal += 1
                    resultado = cuentaRandom(numMin, numMax)
                    respuesta = int(input("Respuesta: "))
                    
                    if respuesta == resultado:
                        print("Acertaste!")
                        racha += 1
                        acierto += 1
                        aciertosTotal += 1
                    else:
                        print(f"Fallaste, el resultado era {resultado}")
                        racha = 0
                        fallo += 1
                        fallosTotal += 1
                        vidas -= 1
                        print(f"Vidas restantes: {vidas}")
                    
                    if racha == 3 and not bronce:
                        bronce = True
                        print("CONSEGUIDO!!: bronce")
                    if racha == 7 and not plata:
                        plata = True
                        print("CONSEGUIDO!!: plata")
                    if racha == 10 and not oro:
                        oro = True
                        print("CONSEGUIDO!!: oro")
                    if numMin > 10 and numMax > 15 and racha == 10:
                        platino = True
                        print("CONSEGUIDO!!: platino")
                except ValueError:
                    print("Error: Debes introducir un número valido.")
                except Exception as error:
                    print(f"Se ha producido un error: {error}")
            
            numJugadas += 1
            print(f"En tu partida numero {numJugadas} acertaste {acierto} operaciones y has fallado {fallo}")
            print(f"Acertaste un porcentaje {round(acierto * 100 / operacionTotal, 2)}% de las cuentas")

        case "2":   
            while True:
                configuracion(vidasConf, numMin, numMax)
                seleccionMenu = input("Que deseas hacer? ")
                
                match seleccionMenu:
                    case "1":
                        try:
                            vidasConf = int(input("Entre 1 y 10: "))
                            while vidasConf < 1 or vidasConf > 10:
                                print("El número de vidas debe estar entre 1 y 10.")
                                vidasConf = int(input("Entre 1 y 10: "))
                        except ValueError:
                            print("Error: Debes introducir un número valido.")
                        except Exception as error:
                            print(f"Se ha producido un error: {error}")
                    
                    case "2":
                        try:
                            numMin = int(input("Nuevo minimo: "))
                            while numMin > numMax:
                                print("NumMin tiene que ser menor que NumMax.")
                                numMin = int(input("Nuevo minimo: "))
                        except ValueError:
                            print("Error: Debes introducir un número valido.")
                        except Exception as error:
                            print(f"Se ha producido un error: {error}")
                    
                    case "3":
                        try:
                            numMax = int(input("Nuevo maximo: "))
                            while numMax < numMin:
                                print("NumMax tiene que ser mayor que NumMin.")
                                numMax = int(input("Nuevo maximo: "))
                        except ValueError:
                            print("Error: Debes introducir un número valido.")
                        except Exception as error:
                            print(f"Se ha producido un error: {error}")
                    
                    case "0":
                        break


        case "3":
            estadisticas(numJugadas, operacionTotal, aciertosTotal, fallosTotal, rachaMax)

        case "4":
            logros(bronce, plata, oro, platino)

        case "0":
            break
