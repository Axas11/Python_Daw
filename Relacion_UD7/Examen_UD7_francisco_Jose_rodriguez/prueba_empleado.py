from empleado import Empleado
from datetime import datetime
empleados = [
    Empleado("Antonio Banderas", "12345678A", datetime(1985, 5, 20), False, False, 2500.0, datetime(2010, 3, 15),[datetime(2023, 1, 1), datetime(2024, 6, 1)]),
    Empleado("El falillo", "87654321B", datetime(1990, 8, 12), True, False, 2800.0, datetime(2015, 6, 20),[datetime(2022, 11, 1)]),
    Empleado("Pedro Sánchez", "11223344C", datetime(1975, 3, 5), False, True, 2300.0, datetime(2008, 1, 10),[]),
    Empleado("Antonio Jose Patilla", "44332211D", datetime(1995, 1, 30), False, False, 3000.0, datetime(2020, 9, 5),[datetime(2023, 2, 1), datetime(2024, 1, 1), datetime(2024, 12, 1)])
]

for empleado in empleados:
    print(empleado)