from ModeloCoche import ModeloCoche

coches = [
    ModeloCoche("Toyota", "Yaris", 2022, 1050, "Gasolina", 116, True, 5, 5, 5.0, 40),
    ModeloCoche("Toyota", "Yaris", 2022, 1050, "Gasolina", 116, True, 5, 5, 5.0, 40),
    ModeloCoche("Volkswagen", "Golf", 2021, 1350, "Diesel", 150, False, 5, 5, 4.5, 50),
    ModeloCoche("BMW", "X5", 2023, 2100, "Hibrido", 286, True, 5, 5, 6.5, 80),
    ]
coches2 = [
    ModeloCoche("Toyota", "Yaris", 2022, 1050, "Gasolina", 116, True, 5, 5, 5.0, 40),
    ModeloCoche("Toyota", "Yaris", 2022, 1050, "Gasolina", 116, True, 5, 5, 5.0, 40),
    ModeloCoche("Volkswagen", "Golf", 2021, 1350, "Diesel", 150, False, 5, 5, 4.5, 50),
    ModeloCoche("BMW", "X5", 2023, 2100, "Hibrido", 286, True, 5, 5, 6.5, 80),
    ]





for coche in coches:
    print(coche.autonomia())


