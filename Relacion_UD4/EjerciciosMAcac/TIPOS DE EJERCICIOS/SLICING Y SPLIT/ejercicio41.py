# A partir de la lista del ejemplo muestra (utilizando slicing) los equipos que irán a la Champions League (los cuatro primeros), los que irán a la UEFA (quinto y sexto) y los que descenderán (los tres últimos). 
liga = ["Real Madrid", "Atlético de Madrid", "FC Barcelona", "Athletic Club","Villarreal CF","Rayo Vallecano","Girona FC","CA Osasuna","RCD Mallorca","Real Betis Balompié","Real Sociedad","Celta de Vigo","Sevilla FC","Getafe CF","UD Las Palmas","RCD Espanyol","CD Leganés","Valencia CF","Deportivo Alavés","Real Valladolid"]
print(f"A la champions van: {liga[0:4]}")
print(f"A la UEFA van: {liga[4:6]}")
print(f"A segunda van: {liga[-3:]}")