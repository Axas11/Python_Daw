# Crea un programa para gestionar una lista de tareas pendientes. La lista comenzará con las siguientes tareas: ["Comprar fruta", "Estudiar programación", "Desinstalar el LOL"]. El programa permitirá ver la lista de tareas pendientes e insertar nuevas tareas en la posición que se desee. 
#  se puedan completar tareas y que al hacerlo desaparezcan de la lista. En concreto cuando se muestren las tareas pendientes haz que si el usuario inserta un número de tarea válido (0 para salir al menú principal) se complete dicha tarea
Tareas = ["Comprar fruta", "Estudiar programación", "Desinstalar el LOL"]


def menu():
    print("Bienvenido a la app de listas to_do más avanzada del universo")
    print("1. Ver tareas pendientes")
    print("2. Agregar tarea pendiente")
    print("0. Salir")


while True:
    menu()
    eleccion = int(input("Que quieres hacer? "))
    match eleccion:
        case 0:
            break
        case 1:
            print("-----------")
            print("Lista de tareas pendientes: ")
            for i, tarea in enumerate(Tareas):
                print(f"{i+1}. {tarea}")
            print("-----------")
            numTareaCompletada = int(input("Has completado alguna tarea? "))
            if numTareaCompletada > 0 and numTareaCompletada < len(Tareas) +1:
                Tareas.pop(numTareaCompletada-1)
                print("Eres un crack! un pikito? ")
            elif numTareaCompletada > len(Tareas) +1:
                print("Tarea no valida")
            else:
                print("No hay Tareas")
            print("-----------")
            print("Lista de tareas pendientes: ")
            for i, tarea in enumerate(Tareas):
                print(f"{i+1}. {tarea}")
            print("-----------")
            if numTareaCompletada == 0:
                break
        case 2:
            nuevaTarea = input("Que tarea quieres insertar? ")
            posicion = int(input("En que posición? "))

            Tareas.insert(posicion, nuevaTarea)
