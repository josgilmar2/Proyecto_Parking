from parking.models.cliente_abonado import ClienteAbonado
from datetime import datetime


class ZonaAdminService:

    def __init__(self, cliente_abonado_service):
        self.__cliente_abonado_service = cliente_abonado_service

    @property
    def cliente_abonado_service(self):
        return self.__cliente_abonado_service

    @cliente_abonado_service.setter
    def cliente_abonado_service(self, cliente_abonado_service):
        self.__cliente_abonado_service = cliente_abonado_service

    def dar_de_alta_a_un_cliente_abonado(self, dni, nombre, apellidos, num_tarjeta, tipo, email, vehiculo, plaza):
        if tipo == 1:
            cliente_abonado = ClienteAbonado(dni, nombre, apellidos, num_tarjeta, tipo, email, datetime.now(),
                                             datetime.now().replace(month=+1), vehiculo, plaza)
            self.cliente_abonado_service.annadir_cliente_abonado(cliente_abonado)
            return True
        elif tipo == 2:
            cliente_abonado = ClienteAbonado(dni, nombre, apellidos, num_tarjeta, tipo, email, datetime.now(),
                                             datetime.now().replace(month=+3), vehiculo, plaza)
            self.cliente_abonado_service.annadir_cliente_abonado(cliente_abonado)
            return True
        elif tipo == 3:
            cliente_abonado = ClienteAbonado(dni, nombre, apellidos, num_tarjeta, tipo, email, datetime.now(),
                                             datetime.now().replace(month=+6), vehiculo, plaza)
            self.cliente_abonado_service.annadir_cliente_abonado(cliente_abonado)
            return True
        elif tipo == 4:
            cliente_abonado = ClienteAbonado(dni, nombre, apellidos, num_tarjeta, tipo, email, datetime.now(),
                                             datetime.now().replace(year=+1), vehiculo, plaza)
            self.cliente_abonado_service.annadir_cliente_abonado(cliente_abonado)
            return True
        return False
