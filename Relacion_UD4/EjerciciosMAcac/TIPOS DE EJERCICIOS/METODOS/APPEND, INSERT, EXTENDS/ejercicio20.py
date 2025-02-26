# Crea un programa para gestionar una lista de tareas pendientes. La lista comenzará con las siguientes tareas: ["Comprar fruta", "Estudiar programación", "Desinstalar el LOL"]. El programa permitirá ver la lista de tareas pendientes e insertar nuevas tareas en la posición que se desee. 
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
            print("Lista de tareas pendientes: ")
            for i, tarea in enumerate(Tareas):
                print(f"{i+1}. {tarea}")
            print("-----------")
        case 2:
            nuevaTarea = input("Que tarea quieres insertar? ")
            posicion = int(input("En que posición? "))
            
            Tareas.insert(posicion -1, nuevaTarea)
