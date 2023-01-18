import pickle


class PlazaService:

    def __init__(self, lista_plazas):
        self.__lista_plazas = lista_plazas

    @property
    def lista_plazas(self):
        return self.__lista_plazas

    @lista_plazas.setter
    def lista_plazas(self, lista_plazas):
        self.__lista_plazas = lista_plazas

    def annadir_plaza(self, plaza):
        self.lista_plazas.append(plaza)
        fichero_plaza = open("./data/plazas", "wb")
        pickle.dump(self.lista_plazas, fichero_plaza)
        fichero_plaza.close()

    def buscar_por_num_plaza(self, num_plaza):
        fichero_plaza = open("./data/plazas", "rb")
        datos_plaza = pickle.load(fichero_plaza)
        for i in datos_plaza:
            if i.num_plaza == num_plaza:
                return i
        return None

    def buscar_por_num_plaza_con_su_pin(self, num_plaza, pin):
        plaza = self.buscar_por_num_plaza(num_plaza)
        if plaza.pin == pin:
            return plaza
        return None
