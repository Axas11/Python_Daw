#Ejercicio 7 (2 puntos). Dada la siguiente matriz:
#En la que la primera columna es el nombre del planeta, la segunda si es rocoso (True) o gaseoso (False) y la tercera su radio. 
#Calcula (utilizando bucles, condicionales y/o métodos/funciones de las listas):
#El radio medio de los planetas gaseosos
#El radio medio de los planetas rocosos
#Si hay algún planeta rocoso que sea más grande que uno gaseoso
#El nombre de los planetas del sistema solar que termina en “no”
planetas = [
    ["Mercurio", True, 2439.7],
    ["Venus", True, 6051.8],
    ["Tierra", True, 6371.0],
    ["Marte", True, 3389.5],
    ["Júpiter", False, 69911],
    ["Saturno", False, 58232],
    ["Urano", False, 25362],
    ["Neptuno", False, 24622],
    ["Plutón", True, 1188.3]
]

media_total = 0
media_gaseosos = 0
cantidad_gaseosos = 0
cantidad_rocosos = 0
media_rocosos = 0
planetas_terminan_no = []

for fila in planetas:
    for elemento in fila:
        radio = fila[2:]
        media = sum(radio)/len(radio)
    media_total += media /len(planetas)

for fila in planetas:
    if fila[1] == True:
        radio = fila[2]
        media_gaseosos += radio
        cantidad_gaseosos += 1
    if fila[0].endswith("no"):
        planetas_terminan_no.append(fila[0])

if cantidad_gaseosos > 0:
     media_gaseoso = media_gaseosos / cantidad_gaseosos
else:
    media_gaseoso = 0

for fila in planetas:
    if fila[1] == False:
        radio = fila[2]
        media_rocosos += radio
        cantidad_rocosos += 122

if cantidad_rocosos > 0:
     media_rocosos = media_rocosos / cantidad_rocosos
else:
    media_rocosos = 0

print(f"La media de los planetas gaseosos es: {media_gaseoso}")
print(f"La media de los planetas gaseosos es: {media_rocosos}")
print(f"La media total de el radio de los planetas es: {media_total}")
print(f"Planetas que terminan en no: {planetas_terminan_no}")

