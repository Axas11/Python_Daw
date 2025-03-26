from datetime import datetime
class ModeloCoche:

    def __init__(self, marca: str, modelo: str, ano_fabricacion: datetime, peso: int, tipo_motor: str, potencia: int, automatico: bool, num_puertas: int, num_asientos: int, consumo: float, deposito: float):
        self.marca = marca
        self.modelo = modelo
        self.ano_fabricacion = ano_fabricacion
        self.peso = peso
        self.tipo_motor = tipo_motor
        self.potencia = potencia
        self.automatico = automatico
        self.num_puertas = num_puertas
        self.num_asientos = num_asientos
        self.consumo = consumo
        self.deposito = deposito

    def peso(self) -> int:
        pesos = ["ligero", "medio", "pesado"]
        if self.peso < 1200:
            peso = pesos[0]
        elif self.peso <= 1200 and self.peso >1800:
            peso = pesos[1]
        else:
            peso = pesos[2]
        return peso
        
    def __str__(self):
        return(
            f"marca: {self.marca}\n"
            f"modelo: {self.modelo} "
            f"ano_fabricacion: {self.ano_fabricacion} "
            f"peso: {self.peso} "
            f"tipo_motor: {self.tipo_motor} "
            f"potencia: {self.potencia} "
            f"automatico: {self.automatico} "
            f"puertas {self.num_puertas} "
            f"asientos {self.num_asientos} "
            f"consumo {self.consumo} "
            f"deposito {self.deposito} "
        )
    
    def autonomia(self) -> float:
        return round(((self.deposito/self.consumo)*100))

