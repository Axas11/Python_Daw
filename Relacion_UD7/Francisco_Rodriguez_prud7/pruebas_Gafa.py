from Gafa import Gafa
from datetime import datetime


g1 = Gafa("Ray-Ban", "RB001", datetime(2022, 5, 1), ["negro", "azul"])
g2 = Gafa("Oakley", "OX3218", datetime(2023, 3, 15), ["rojo"])
g3 = Gafa("Ray-Ban", "RB001", datetime(2021, 1, 10), ["gris", "verde"])


print(g1)
print(g1 == g2)
print(g1 == g3)
