from parking.models.turismo import Turismo
from parking.models.motocicleta import Motocicleta
from parking.models.movilidad_reducida import MovilidadReducida
from datetime import timedelta


class Ticket:

    def __init__(self, vehiculo, pago_realizado):
        self.__vehiculo = vehiculo
        self.__pago_realizado = pago_realizado

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    @property
    def pago_realizado(self):
        return self.__pago_realizado

    @pago_realizado.setter
    def pago_realizado(self, pago_realizado):
        self.__pago_realizado = pago_realizado

    def __str__(self):
        if not self.pago_realizado:
            return "\nPARKING JLGM \n" \
                  "-------------------------------------------------- \n" \
                  f"Matrícula: {self.vehiculo.matricula} \n" \
                   f"Número de plaza: {self.vehiculo.plaza.num_plaza} \n" \
                  f"Fecha de depósito: ´{self.vehiculo.fecha_deposito} \n" \
                  f"PIN: {self.vehiculo.plaza.pin}\n" \
                   f"-----------------------------------------------"
        else:
            return "\nPARKING JLGM \n" \
                  "------------------------------------------------- \n" \
                  f"Matrícula: {self.vehiculo.matricula} \n" \
                  f"Fecha de depósito: ´{self.vehiculo.fecha_deposito} \n" \
                  f"Fecha salida: {self.vehiculo.fecha_salida} \n" \
                  f"Tarifa a pagar: {self.calcular_tarifa_a_pagar(self.vehiculo)} \n" \
                   f"-----------------------------------------------\n"

    def calcular_tarifa_a_pagar(self, vehiculo):
        tiempo_estacionado = divmod((vehiculo.fecha_salida - vehiculo.fecha_deposito).total_seconds(), 60)[0]
        if type(vehiculo) == Turismo:
            return tiempo_estacionado * 0.12
        elif type(vehiculo) == Motocicleta:
            return tiempo_estacionado * 0.08
        elif type(vehiculo) == MovilidadReducida:
            return tiempo_estacionado * 0.1