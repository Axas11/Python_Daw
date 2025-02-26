# Crea un programa que lea palabras hasta que insertes la palabra ‘fin’. Una vez se inserte ‘fin’ se mostrarán las palabras introducidas en orden alfabético (‘fin’ no debe contar). 
palabras = []
while True: 
    n = input("Iserta una palabra (fin para terminar): ")
    if n == "fin":
        break
    else:
        palabras.append(n)

palabras.sort()
print(palabras)