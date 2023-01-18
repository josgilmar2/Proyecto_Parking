from parking.models.parking import Parking
from parking.models.plaza import Plaza
from parking.models.turismo import Turismo
from parking.models.motocicleta import Motocicleta
from parking.models.movilidad_reducida import MovilidadReducida
from datetime import datetime
import random


class ParkingService:

    def __init__(self, parking):
        self.__parking = parking

    @property
    def parking(self):
        return self.__parking

    @parking.setter
    def parking(self, parking):
        self.__parking = parking

    def actualizar_parking(self):
        plaza_turismo = 0
        plaza_motocicleta = 0
        plaza_movilidad_reducida = 0
        for i in self.parking.lista_vehiculos:
            if type(i) == Turismo:
                plaza_turismo += 1
            if type(i) == Motocicleta:
                plaza_motocicleta += 1
            if type(i) == MovilidadReducida:
                plaza_movilidad_reducida += 1
        self.parking.plazas_libres = int(self.parking.plazas_totales) - int(len(self.parking.lista_vehiculos))
        self.parking.plazas_turismo -= plaza_turismo
        self.parking.plazas_motocicleta -= plaza_motocicleta
        self.parking.plazas_movilidad_reducida -= plaza_movilidad_reducida

    def ver_plazas_parking(self):
        self.actualizar_parking()
        return f"Quedan un total de {self.parking.plazas_libres} plazas de las cuales: \n" \
               f"{self.parking.plazas_turismo} son para TURISMOS \n" \
               f"{self.parking.plazas_motocicleta} son para MOTOCICLETAS \n" \
               f"{self.parking.plazas_movilidad_reducida} son para MOVILIDAD REDUCIDA"