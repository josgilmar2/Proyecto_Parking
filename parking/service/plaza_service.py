import pickle


class PlazaService:

    def __init__(self, plaza_pickle=open("./pickle/plaza_pickle", "rb"), lista_plazas=[]):
        self.__plaza_pickle = plaza_pickle
        self.__lista_plazas = lista_plazas

    @property
    def plaza_pickle(self):
        return self.__plaza_pickle

    @plaza_pickle.setter
    def plaza_pickle(self, plaza_pickle):
        self.__plaza_pickle = plaza_pickle

    @property
    def lista_plazas(self):
        return self.__lista_plazas

    @lista_plazas.setter
    def lista_plazas(self, lista_plazas):
        self.__lista_plazas = lista_plazas

    def annadir_plaza_pickle(self):
        self.plaza_pickle.close()
        fichero_plaza_annadir = open("./pickle/plaza_pickle", "wb")
        pickle.dump(self.lista_plazas, fichero_plaza_annadir)
        fichero_plaza_annadir.close()
        self.plaza_pickle = open("./pickle/plaza_pickle", "rb")

    def annadir_plaza(self, plaza):
        self.lista_plazas.append(plaza)
        return self.annadir_plaza_pickle()

    def buscar_por_num_plaza(self, num_plaza):
        datos_plaza = pickle.load(self.__plaza_pickle)
        for i in datos_plaza:
            if i.num_plaza == num_plaza:
                return i
        return None

    def buscar_por_pin(self, num_plaza, pin):
        plaza = self.buscar_por_num_plaza(num_plaza)
        if plaza.pin == pin:
            return plaza
        return None
