class Parking:

    def __init__(self, lista_vehiculos, plazas_totales, plazas_turismo, plazas_motocicleta, plazas_movilidad_reducida):
        self.__lista_vehiculos = lista_vehiculos
        self.__plazas_totales = plazas_totales
        self.__plazas_libres = len(lista_vehiculos)
        self.__plazas_turismo = plazas_turismo
        self.__plazas_motocicleta = plazas_motocicleta
        self.__plazas_movilidad_reducida = plazas_movilidad_reducida

    @property
    def lista_vehiculos(self):
        return self.__lista_vehiculos

    @lista_vehiculos.setter
    def lista_vehiculos(self, lista_vehiculos):
        self.__lista_vehiculos = lista_vehiculos

    @property
    def plazas_totales(self):
        return self.__plazas_totales

    @plazas_totales.setter
    def plazas_totales(self, plazas_totales):
        self.__plazas_totales = plazas_totales

    @property
    def plazas_libres(self):
        return self.__plazas_libres

    @plazas_libres.setter
    def plazas_libres(self, plazas_libres):
        self.__plazas_libres = plazas_libres

    @property
    def plazas_turismo(self):
        return self.__plazas_turismo

    @plazas_turismo.setter
    def plazas_turismo(self, plazas_turismo):
        self.__plazas_turismo = plazas_turismo

    @property
    def plazas_motocicleta(self):
        return self.__plazas_motocicleta

    @plazas_motocicleta.setter
    def plazas_motocicleta(self, plazas_motocicleta):
        self.__plazas_motocicleta = plazas_motocicleta

    @property
    def plazas_movilidad_reducida(self):
        return self.__plazas_movilidad_reducida

    @plazas_movilidad_reducida.setter
    def plazas_movilidad_reducida(self, plazas_movilidad_reducida):
        self.__plazas_movilidad_reducida = plazas_movilidad_reducida

    def __str__(self):
        return f"El parking tiene un total de {self.plazas_totales} plazas de las cuales: \n" \
               f"{self.plazas_turismo} plazas son para turismo \n" \
               f"{self.plazas_motocicleta} plazas son para motocicleta \n" \
               f"{self.plazas_movilidad_reducida} plazas son para movilidad reducida \n"


