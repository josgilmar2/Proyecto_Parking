class Vehiculo:
    def __init__(self, matricula, fecha_deposito, fecha_salida, plaza):
        self.__matricula = matricula
        self.__fecha_deposito = fecha_deposito
        self.__fecha_salida = fecha_salida
        self.__plaza = plaza

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def fecha_deposito(self):
        return self.__fecha_deposito

    @fecha_deposito.setter
    def fecha_deposito(self, fecha_deposito):
        self.__fecha_deposito = fecha_deposito

    @property
    def fecha_salida(self):
        return self.__fecha_salida

    @fecha_salida.setter
    def fecha_salida(self, fecha_salida):
        self.__fecha_salida = fecha_salida

    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, plaza):
        self.__plaza = plaza