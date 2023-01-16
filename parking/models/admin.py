class Admin:

    def __init__(self, usuario, contrasenna):
        self.__usuario = usuario
        self.__contrasenna = contrasenna

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def contrasenna(self):
        return self.__contrasenna

    @contrasenna.setter
    def contrasenna(self, contrasenna):
        self.__contrasenna = contrasenna
