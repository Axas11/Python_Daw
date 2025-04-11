    
def edad(self)->int:
    fecha_actual = datetime.now()
    return fecha_actual.year - self.fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))