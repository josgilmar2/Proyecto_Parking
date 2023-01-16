from parking.models.vehiculo import Vehiculo


class Motocicleta(Vehiculo):
    def __init__(self, matricula, fecha_deposito, fecha_salida, plaza, tarifa=0.08):
        super().__init__(matricula, fecha_deposito, fecha_salida, plaza)
        self.__tarifa = tarifa

    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def tarifa(self, tarifa):
        self.__tarifa = tarifa