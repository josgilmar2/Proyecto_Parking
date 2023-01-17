import pickle


class VehiculoService:

    def __init__(self, vehiculo_pickle=open("./pickle/vehiculo_pickle", "rb"), lista_vehiculos=[]):
        self.__vehiculo_pickle = vehiculo_pickle
        self.__lista_vehiculos = lista_vehiculos

    @property
    def vehiculo_pickle(self):
        return self.__vehiculo_pickle

    @vehiculo_pickle.setter
    def vehiculo_pickle(self, vehiculo_pickle):
        self.__vehiculo_pickle = vehiculo_pickle

    @property
    def lista_vehiculos(self):
        return self.__lista_vehiculos

    @lista_vehiculos.setter
    def lista_vehiculos(self, lista_vehiculos):
        self.__lista_vehiculos = lista_vehiculos

    def annadir_vehiculo_pickel(self):
        self.vehiculo_pickle.close()
        fichero_vehiculo_annadir = open("./pickle/vehiculo_pickle", "wb")
        pickle.dump(self.lista_vehiculos, fichero_vehiculo_annadir)
        fichero_vehiculo_annadir.close()
        self.vehiculo_pickle = open("./pickle/vehiculo_pickle", "rb")

    def annadir_vehiculo(self, vehiculo):
        self.lista_vehiculos.append(vehiculo)
        return self.annadir_vehiculo_pickel()

    def buscar_por_matricula(self, matricula):
        datos_vehiculo = pickle.load(self.vehiculo_pickle)
        for i in datos_vehiculo:
            if i.matricula == matricula:
                return i
        return None
