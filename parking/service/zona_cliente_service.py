from datetime import datetime, timedelta
import random

from parking.models.turismo import Turismo
from parking.models.motocicleta import Motocicleta
from parking.models.movilidad_reducida import MovilidadReducida
from parking.models.plaza import Plaza


class ZonaClienteService:

    def __init__(self, parking_service, vehiculo_service, plaza_service, ticket_service):
        self.__parking_service = parking_service
        self.__vehiculo_service = vehiculo_service
        self.__plaza_service = plaza_service
        self.__ticket_service = ticket_service

    @property
    def parking_service(self):
        return self.__parking_service

    @parking_service.setter
    def parking_service(self, parking_service):
        self.__parking_service = parking_service

    @property
    def vehiculo_service(self):
        return self.__vehiculo_service

    @vehiculo_service.setter
    def vehiculo_service(self, vehiculo_service):
        self.__vehiculo_service = vehiculo_service

    @property
    def plaza_service(self):
        return self.__plaza_service

    @plaza_service.setter
    def plaza_service(self, plaza_service):
        self.__plaza_service = plaza_service

    @property
    def ticket_service(self):
        return self.__ticket_service

    @ticket_service.setter
    def ticket_service(self, ticket_service):
        self.__ticket_service = ticket_service

    def generar_num_plaza_turismo(self, parking):
        for i in parking.lista_vehiculos:
            num_plaza = random.randint(1, 56)
            while i.plaza.num_plaza == num_plaza:
                num_plaza = random.randint(1, 56)
        return num_plaza

    def generar_num_plaza_motocicleta(self, parking):
        for i in parking.lista_vehiculos:
            num_plaza = random.randint(57, 68)
            while i.plaza.num_plaza == num_plaza:
                num_plaza = random.randint(57, 68)
        return num_plaza

    def generar_num_plaza_movilidad_reducida(self, parking):
        for i in parking.lista_vehiculos:
            num_plaza = random.randint(68, 80)
            while i.plaza.num_plaza == num_plaza:
                num_plaza = random.randint(68, 80)
        return num_plaza

    def asignar_vehiculo_a_una_plaza(self, vehiculo):
        parking = self.parking_service.parking
        self.parking_service.actualizar_parking(parking)
        if 0 < parking.plazas_libres <= parking.plazas_totales:
            if type(vehiculo) is Turismo:
                plaza = Plaza(self.generar_num_plaza_turismo(parking), random.randint(100000, 999999), True, vehiculo)
                plaza.vehiculo = vehiculo
                vehiculo.plaza = plaza
                vehiculo.fecha_deposito = datetime.now()
                vehiculo.fecha_salida = None
                self.plaza_service.annadir_plaza(plaza)
                return True
            if type(vehiculo) is Motocicleta:
                plaza = Plaza(self.generar_num_plaza_motocicleta(parking), round(random.randint(100000, 999999)), True, vehiculo)
                plaza.vehiculo = vehiculo
                vehiculo.plaza = plaza
                vehiculo.fecha_deposito = datetime.now()
                self.plaza_service.annadir_plaza(plaza)
                return True
            if type(vehiculo) is MovilidadReducida:
                plaza = Plaza(self.generar_num_plaza_movilidad_reducida(parking), round(random.randint(100000, 999999)), True, vehiculo)
                plaza.vehiculo = vehiculo
                vehiculo.plaza = plaza
                vehiculo.fecha_deposito = datetime.now()
                self.plaza_service.annadir_plaza(plaza)
                return True
        return False

    def depositar_vehiculo_normal(self, vehiculo):
        if self.asignar_vehiculo_a_una_plaza(vehiculo):
            self.ticket_service.crear_ticket_llegada(vehiculo)
            self.vehiculo_service.annadir_vehiculo(vehiculo)
            return print("El vehículo se ha depositado correctamente\n")
        else:
            return print("El vehículo NO se ha depositado correctamente\n")

    def retirar_vehiculo_normal(self, matricula, num_plaza, pin):
        vehiculo = self.vehiculo_service.buscar_por_matricula(matricula)
        plaza = self.plaza_service.buscar_por_num_plaza_con_su_pin(num_plaza, pin)
        if plaza.__eq__(vehiculo.plaza):
            vehiculo.plaza = None
            plaza.vehiculo = None
            vehiculo.fecha_salida = datetime.now()
            plaza.ocupada = False
            return self.ticket_service.crear_ticket_salida(vehiculo)

    def depositar_vehiculo_abonado(self, cliente_abonado, pin):
        if cliente_abonado.plaza.pin == pin:
            cliente_abonado.vehiculo.plaza = cliente_abonado.plaza
            cliente_abonado.plaza.ocupada = True
            cliente_abonado.vehiculo.fecha_deposito = datetime.now()
            return f"\nEl vehículo se ha depositado correctamente. Disfrute de la estancia " \
                   f"{cliente_abonado.nombre} {cliente_abonado.apellidos}\n "

    def retirar_vehiculo_abonado(self, cliente_abonado, pin):
        if cliente_abonado.plaza.pin == pin:
            cliente_abonado.vehiculo.plaza = None
            cliente_abonado.vehiculo.fecha_salida = datetime.now()
            return f"\nEl vehículo se ha retirado correctamente. Muchas gracias por seguir confiando en " \
                   f"nuestro parking {cliente_abonado.nombre} {cliente_abonado.apellidos}"
