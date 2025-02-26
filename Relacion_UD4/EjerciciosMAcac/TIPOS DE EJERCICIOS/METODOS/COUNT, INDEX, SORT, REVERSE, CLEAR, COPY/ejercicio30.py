# Crea un programa que contenga 3 listas: una con el nombre de los 8 planetas del Sistema Solar, 
# otra con sus respectivas masas y otra con sus respectivos radios. Cuando insertes por teclado el nombre de un planeta 
# el programa deberá dar la siguiente información: su posición en el Sistema Solar, su masa y su radio. 
planetas_sistema_solar = [
   "Mercurio", "Venus", "Tierra", "Marte",
   "Júpiter", "Saturno", "Urano", "Neptuno"
]

masas_sistema_solar = [
   3.3011e23,  # Mercurio
   4.8675e24,  # Venus
   5.97237e24,  # Tierra
   6.4171e23,  # Marte
   1.8982e27,  # Júpiter
   5.6834e26,  # Saturno
   8.6810e25,  # Urano
   1.02413e26  # Neptuno
]

radio_planetas = [
    2.440,  #Mercurio
    6.052,  #Venus
    6.371,  #Tierra
    3.390,  #Marte
    69.911, #Jupiter
    58.232, #Saturno
    25.362, #Urano
    24.622, #Neptuno
]

planeta = input("Inserta un planeta: ")

posicion = planetas_sistema_solar.index(planeta)+1
masa = masas_sistema_solar[planetas_sistema_solar.index(planeta)]
radio = radio_planetas[planetas_sistema_solar.index(planeta)]

print(f"La posicion de {planeta} es {posicion}")
print(f"La masa de {planeta} es {masa}")
print(f"El radio de {planeta} es {radio}") 