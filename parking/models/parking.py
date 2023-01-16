class Parking():

    def __init__(self, lista_turismos, lista_motocicletas, lista_movilidad_reducida, plazas_totales=80):
        self.__listaMotocicletas = lista_motocicletas
        self.__listaTurismos = lista_turismos
        self.__lista_minusvalidos = lista_movilidad_reducida
        self.__plazas_totales = plazas_totales

    @property
    def lista_turismos(self):
        return self.__listaTurismos

    @lista_turismos.setter
    def lista_turismos(self, lista_turismos):
        self.__lista_turismos = lista_turismos

    @property
    def lista_motocicletas(self):
        return self.__listaMotocicletas

    @lista_motocicletas.setter
    def lista_motocicletas(self, lista_motocicletas):
        self.__lista_motocicletas = lista_motocicletas

    @property
    def lista_movilidad_reducida(self):
        return self.__lista_minusvalidos

    @lista_movilidad_reducida.setter
    def lista_movilidad_reducida(self, lista_movilidad_reducida):
        self.__lista_minusvalidos = lista_movilidad_reducida

    @property
    def plazas_totales(self):
        return self.__plazas_totales

    @plazas_totales.setter
    def plazas_totales(self, plazas_totales):
        self.__plazas_totales = plazas_totales

    def __str__(self):
        for i in self.lista_turismos:
            print(i)
        for i in self.lista_motocicletas:
            print(i)
        for i in self.lista_movilidad_reducida:
            print(i)
        return ""
