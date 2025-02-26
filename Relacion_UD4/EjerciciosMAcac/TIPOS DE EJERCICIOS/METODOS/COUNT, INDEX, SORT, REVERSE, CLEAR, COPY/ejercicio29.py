# Crea un programa que tenga una lista con los equipos de la liga de fútbol ordenados según su posición en la liga. Haz que el programa lea el nombre de equipos por teclado, si el equipo existe devolverá su posición en la clasificación si no existe se informará que dicho equipo no existe pero el programa NO debe fallar. 
liga = ["Real Madrid", "Atlético de Madrid", "FC Barcelona", "Athletic Club",  "Villarreal CF", "RCD Mallorca", "Rayo Vallecano", "Girona FC", "Real Sociedad", "Real Betis", "CA Osasuna", "Sevilla FC", "RC Celta", "Getafe CF", "UD Las Palmas", "CD Leganés", "Deportivo Alavés", "RCD Espanyol", "Valencia CF", "Real Valladolid"]

equipo = input("Di un equipo de la liga: ")
if equipo in liga:
    print(f"El {equipo} se encuentra en la posición {liga.index(equipo)+1} de la liga")
else:
    print(f"El {equipo} no existe en la liga")