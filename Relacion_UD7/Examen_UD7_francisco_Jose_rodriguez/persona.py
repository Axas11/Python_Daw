#Crea la clase persona con los siguientes atributos: nombre (str), dni (str), fecha_nacimiento (datetime),  casado (bool) y divorciado (bool)
from datetime import datetime
class Persona:
    def __init__(self, nombre:str, dni:str, fecha_nacimiento:datetime, casado:bool, divorciado:bool):
        self.nombre = nombre
        self.dni = dni

        if fecha_nacimiento <= datetime.now():
            self.fecha_nacimiento = fecha_nacimiento
        
        if casado and divorciado:
            self.casado = False
            self.divorciado = False
        else:
            self.casado = casado
            self.divorciado = divorciado
        
    def edad(self)->int:
        fecha_actual = datetime.now()
        return fecha_actual.year - self.fecha_nacimiento.year

    def estado_civil(self) -> str:
        if self.casado:
            return "casado"
        elif self.divorciado:
            return "divorciado"
        else:
            return "soltero"

    def __eq__(self, other)->bool:
        if isinstance(other, Persona):
            return self.dni == other.dni
        return False

    def __str__(self)->str:
        fecha_nac_str = self.fecha_nacimiento
        return f"{self.nombre}\n DNI: {self.dni}, fecha nacimiento: {fecha_nac_str}, edad: {self.edad()}, estado civil: {self.estado_civil()}"   




