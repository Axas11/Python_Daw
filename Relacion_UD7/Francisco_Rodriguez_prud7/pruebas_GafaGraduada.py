from GafaGraduada import GafaGraduada
from datetime import datetime


g1 = GafaGraduada("Ray-Ban", "RB001", datetime(2022, 5, 1), ["negro", "azul"], 1.5, "monofocal", True, 120.0, 5)
g2 = GafaGraduada("Oakley", "OX3218", datetime(2023, 3, 15), ["rojo"], 2.0, "progresivo", False, 180.0, 3)
g3 = GafaGraduada("Vogue", "VG202", datetime(2021, 1, 10), ["dorado", "negro"], 0.75, "monofocal", True, 95.5, 4)


print(g1)
print(g1 == g2)
print(g1 == g3)
print(g1 < g2)
print(g1 <= g1)
print(g2 > g1)
print(g2 >= g2)
