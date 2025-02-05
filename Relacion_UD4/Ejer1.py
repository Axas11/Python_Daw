#Ejercicio 1. Crea una lista con las provincias de Andalucía y muestra por pantalla solo aquellas que empiezan por la letra C. 
andalucia = ["Almería", "Cádiz", "Córdoba", "Granada", "Huelva", "Jaén", "Málaga" , "Sevilla"]
for provincia in andalucia:
    if provincia[0] == "C":
        print (provincia)
