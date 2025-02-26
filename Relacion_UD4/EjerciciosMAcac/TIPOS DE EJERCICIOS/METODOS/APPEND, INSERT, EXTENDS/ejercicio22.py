# Crea una lista con las asignaturas del primer curso DAW y otra con las del segundo curso. Usando .extend crea una tercera lista que contenga todas las asignaturas de DAW. 
PrimeroDaw = ["Bases de Datos", "Entornos de Desarrollo", "FOL", "Lenguajes de Marcas" "Sistemas de Gestión de Información", 
"Programación", "Ingles", "Sostenibilidad", "Digitalizacion"]
SegundoDaw = ["Desarrollo Web en Entorno Cliente", "Desarrollo Web en Entorno Servidor", "Despliegue de Aplicaciones Web",
"Diseño de Interfaces Web", "Empresa e Iniciativa Emprendedora", "Proyecto de Desarrollo de Aplicaciones Web", "Formación en Centros de Trabajo"]

daw = []

daw.extend(PrimeroDaw)
daw.extend(SegundoDaw)
print(f"El ciclo de DAW tiene las siguientes asignaturas: {daw}")
