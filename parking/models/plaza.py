class Plaza:

    def __init__(self, num_plaza, pin, ocupada, reservada, vehiculo):
        self.__num_plaza = num_plaza
        self.__pin = pin
        self.__ocupada = ocupada
        self.__reservada = reservada
        self.__vehiculo = vehiculo

    @property
    def num_plaza(self):
        return self.__num_plaza

    @num_plaza.setter
    def num_plaza(self, num_plaza):
        self.__num_plaza = num_plaza

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @property
    def ocupada(self):
        return self.__ocupada

    @ocupada.setter
    def ocupada(self, ocupada):
        self.__ocupada = ocupada

    @property
    def reservada(self):
        return self.__reservada

    @reservada.setter
    def reservada(self, reservada):
        self.__reservada = reservada

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo
