#Dadas las siguientes listas (la segunda contiene la masa de los planetas), encuentra el nombre del planeta de mayor masa y el de aquellos planetas cuya masa es superior a la masa media del sistema solar. 
import statistics
# Lista con los nombres de los planetas del sistema solar
planetas_sistema_solar = [
   "Mercurio", "Venus", "Tierra", "Marte",
   "Júpiter", "Saturno", "Urano", "Neptuno"
]
# Lista con las masas de los planetas en kilogramos (valores aproximados)
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

print(f"El planeta con mayor masa es: {planetas_sistema_solar[masas_sistema_solar.index(max(masas_sistema_solar))]}")
print(f"Los planetas cuya masa es mayor a la masa media ({statistics.mean(masas_sistema_solar)} kg) son:")
for masa in masas_sistema_solar:
    if masa > statistics.mean(masas_sistema_solar):
        print(f"{planetas_sistema_solar[masas_sistema_solar.index(masa)]}")