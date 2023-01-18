from parking.models.parking import Parking
from parking.models.plaza import Plaza
from parking.models.turismo import Turismo
from parking.models.motocicleta import Motocicleta
from parking.models.movilidad_reducida import MovilidadReducida
from datetime import datetime
import random
import pickle


class ParkingService:

    def __init__(self, parking):
        self.__parking = parking

    @property
    def parking(self):
        return self.__parking

    @parking.setter
    def parking(self, parking):
        self.__parking = parking

    def actualizar_parking(self, parking):
        parking.plazas_turismo = 56
        parking.plazas_motocicleta = 12
        parking.plazas_movilidad_reducida = 12
        for i in parking.lista_vehiculos:
            if type(i) == Turismo:
                parking.plazas_turismo -= 1
            elif type(i) == Motocicleta:
                parking.plazas_motocicleta -= 1
            elif type(i) == MovilidadReducida:
                parking.plazas_movilidad_reducida -= 1

    def ver_plazas_parking(self, parking):
        self.actualizar_parking(parking)
        return f"Quedan un total de {parking.plazas_totales - len(parking.lista_vehiculos)} plazas de las cuales: \n" \
               f"{parking.plazas_turismo} son para TURISMOS \n" \
               f"{parking.plazas_motocicleta} son para MOTOCICLETAS \n" \
               f"{parking.plazas_movilidad_reducida} son para MOVILIDAD REDUCIDA"