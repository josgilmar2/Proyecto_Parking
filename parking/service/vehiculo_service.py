import pickle


class VehiculoService:

    def __init__(self, lista_vehiculos):
        self.__lista_vehiculos = lista_vehiculos

    @property
    def lista_vehiculos(self):
        return self.__lista_vehiculos

    @lista_vehiculos.setter
    def lista_vehiculos(self, lista_vehiculos):
        self.__lista_vehiculos = lista_vehiculos

    def annadir_vehiculo(self, vehiculo):
        self.lista_vehiculos.append(vehiculo)
        fichero_vehiculo = open("./data/vehiculos", "wb")
        pickle.dump(self.lista_vehiculos, fichero_vehiculo)
        fichero_vehiculo.close()

    def buscar_por_matricula(self, matricula):
        fichero_vehiculo = open("./data/vehiculos", "rb")
        datos_vehiculo = pickle.load(fichero_vehiculo)
        fichero_vehiculo.close()
        for i in datos_vehiculo:
            if i.matricula == matricula:
                return i
        return None

