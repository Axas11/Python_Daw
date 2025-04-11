from persona import Persona
from datetime import datetime

p = [
    Persona("Marta López Molina", "75523421H", datetime(1990, 3, 9), True, False),
    Persona("Carlos Antonio Manuel", "22523421H", datetime(1999, 11, 9), True, False),
    Persona("Antonio Jose Patilla", "75523331H", datetime(2000, 5, 9), True, False)
]

for p in p:
    print(p)


