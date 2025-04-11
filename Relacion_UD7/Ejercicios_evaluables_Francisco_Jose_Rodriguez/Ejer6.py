2from dataclasses import dataclass

@dataclass
class Planeta:
    nombre: str
    rocoso: bool
    num_lunas: int

planetas = [
    Planeta("Mercurio", True, 0),
    Planeta("Venus", True, 0),
    Planeta("Tierra", True, 1),
    Planeta("Marte", True, 2),
    Planeta("Júpiter", False, 95),
    Planeta("Saturno", False, 146),
    Planeta("Urano", False, 27),
    Planeta("Neptuno", False, 14),
    Planeta("Plutón", True, 5)
]

for planeta in planetas:
    print(planeta)

planetas_filtrados = [planeta for planeta in planetas if planeta.rocoso == True and planeta.num_lunas == 0]

for planeta in planetas_filtrados:
    print(planeta.nombre)