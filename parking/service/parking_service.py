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

    def generar_pin(self):
        numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        return random.sample(numeros, 6)

    def repartir_plazas(self):
        cantidad_turismos = 56
        cantidad_motocicleta = 12

        for i in range(0, cantidad_turismos):
            plaza_turismo = Plaza(i, self.generar_pin(), False, False, None)
            self.parking.lista_turismos.append(plaza_turismo)

        for i in range(cantidad_turismos, cantidad_turismos + cantidad_motocicleta):
            plaza_motocicleta = Plaza(i, self.generar_pin(), False, False, None)
            self.parking.lista_motocicletas.append(plaza_motocicleta)

        for i in range(cantidad_turismos + cantidad_motocicleta, self.parking.plazas_totales):
            plaza_movilidad_reducida = Plaza(i, self.generar_pin(), False, False, None)
            self.parking.lista_movilidad_reducida.append(plaza_movilidad_reducida)

    def ver_plazas_libres_normales(self):
        plazas_totales_turismo = len(self.parking.lista_turismos)
        plazas_totales_motocicletas = len(self.parking.lista_motocicletas)
        plazas_totales_movilidad_reducida = len(self.parking.lista_movilidad_reducida)

        for i in self.parking.lista_turismos:
            if i.ocupada and i.reservada:
                plazas_totales_turismo -= 1
        for i in self.parking.lista_motocicletas:
            if i.ocupada and i.reservada:
                plazas_totales_motocicletas -= 1
        for i in self.parking.lista_movilidad_reducida:
            if i.ocupada and i.reservada:
                plazas_totales_movilidad_reducida -= 1

        print(f"Hay {plazas_totales_turismo} plazas de TURISMO libre.\n"
              f"Hay {plazas_totales_motocicletas} plazas de MOTOCICLETA libre.\n"
              f"Hay {plazas_totales_movilidad_reducida} plazas de MOVILIDAD REDUCIDA.")

    def comprobar_plaza_turismo(self):
        cont = 0
        for i in self.parking.lista_turismos:
            if not i.ocupada and not i.reservada:
                return cont
            cont += 1
        return -1

    def depositar_turismo(self, matricula):
        if self.comprobar_plaza_turismo() != -1:
            plaza_a_ocupar = self.comprobar_plaza_turismo()
            turismo = Turismo(matricula, datetime.now(), None, plaza_a_ocupar)
            self.parking.lista_turismos[plaza_a_ocupar].vehiculo = turismo
            self.parking.lista_turismos[plaza_a_ocupar].ocupada = True
            return True
        return False

    def comprobar_plaza_motocicleta(self):
        cont = 0
        for i in self.parking.lista_motocicletas:
            if not i.ocupada and not i.reservada:
                return cont
            cont += 1
        return -1

    def depositar_motocicleta(self, matricula):
        if self.comprobar_plaza_motocicleta() != -1:
            plaza_a_ocupar = self.comprobar_plaza_motocicleta()
            motocicleta = Motocicleta(matricula, datetime.now(), None, plaza_a_ocupar)
            self.parking.lista_motocicletas[plaza_a_ocupar].vehiculo = motocicleta
            self.parking.lista_motocicletas[plaza_a_ocupar].ocupada = True
            return True
        return False

    def comprobar_plaza_movilidad_reducida(self):
        cont = 0
        for i in self.parking.lista_movilidad_reducida:
            if not i.ocupada and not i.reservada:
                return cont
            cont += 1
        return -1

    def depositar_movilidad_reducida(self, matricula):
        if self.comprobar_plaza_movilidad_reducida() != -1:
            plaza_a_ocupar = self.comprobar_plaza_movilidad_reducida()
            movilidad_reducida = MovilidadReducida(matricula, datetime.now(), None, plaza_a_ocupar)
            self.parking.lista_movilidad_reducida[plaza_a_ocupar].vehiculo = movilidad_reducida
            self.parking.lista_movilidad_reducida[plaza_a_ocupar].ocupada = True
            return True
        return False
