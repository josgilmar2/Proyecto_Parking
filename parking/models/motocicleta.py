from parking.models.vehiculo import Vehiculo


class Motocicleta(Vehiculo):
    def __init__(self, matricula, fecha_deposito, fecha_salida, plaza):
        super().__init__(matricula, fecha_deposito, fecha_salida, plaza)