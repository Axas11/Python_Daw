from dataclasses import dataclass
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
    Planeta("Jupiter", False, 95),
    Planeta("Saturno", False, 146),
    Planeta("Urano", False, 27),
    Planeta("Neptuno", False, 14),
    Planeta("Pluton", True, 5),
]


for p in planetas:
    print(p)

[print(p) for p in planetas]

[print(p.nombre) for p in planetas if p.rocoso and p.num_lunas == 0]



