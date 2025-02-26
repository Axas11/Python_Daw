#Ejercicio 9. Crea una lista con el nombre de todos los países de Europa. 
#Muestra por pantalla el nombre de aquellos países que tengan 6 o menos letras. 
paises_europa = [
    "Albania", "Alemania", "Andorra", "Armenia", "Austria", "Azerbaiyán",  
    "Bélgica", "Bielorrusia", "Bosnia y Herzegovina", "Bulgaria",  
    "Chipre", "Croacia", "Dinamarca", "Eslovaquia", "Eslovenia",  
    "España", "Estonia", "Finlandia", "Francia", "Georgia",  
    "Grecia", "Hungría", "Irlanda", "Islandia", "Italia",  
    "Kazajistán", "Kosovo", "Letonia", "Liechtenstein", "Lituania",  
    "Luxemburgo", "Malta", "Moldavia", "Mónaco", "Montenegro",  
    "Noruega", "Países Bajos", "Polonia", "Portugal", "Reino Unido",  
    "República Checa", "Macedonia del Norte", "Rumanía", "San Marino",  
    "Serbia", "Suecia", "Suiza", "Ucrania", "Ciudad del Vaticano", "Marruecos"
]

for pais in paises_europa:
    if len(pais) <= 6:
        print(pais)

for pais in paises_europa:
    if pais == "Marruecos":
        print(f"Morrococo {pais}")
