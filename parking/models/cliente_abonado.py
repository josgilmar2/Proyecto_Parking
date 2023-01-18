class ClienteAbonado:

    def __init__(self, dni, nombre, apellidos, num_tarjeta, tipo, email,
                 fecha_activacion, fecha_caducidad, precio_abono, vehiculo, plaza):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__num_tarjeta = num_tarjeta
        self.__tipo = tipo
        self.__email = email
        self.__fecha_activacion = fecha_activacion
        self.__fecha_caducidad = fecha_caducidad
        self.__precio_abono = precio_abono
        self.__vehiculo = vehiculo
        self.__plaza = plaza

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    @property
    def num_tarjeta(self):
        return self.__num_tarjeta

    @num_tarjeta.setter
    def num_tarjeta(self, num_tarjeta):
        self.__num_tarjeta = num_tarjeta

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def fecha_activacion(self):
        return self.__fecha_activacion

    @fecha_activacion.setter
    def fecha_activacion(self, fecha_activacion):
        self.__fecha_activacion = fecha_activacion

    @property
    def fecha_caducidad(self):
        return self.__fecha_caducidad

    @fecha_caducidad.setter
    def fecha_caducidad(self, fecha_caducidad):
        self.__fecha_caducidad = fecha_caducidad

    @property
    def precio_abono(self):
        return self.__precio_abono

    @precio_abono.setter
    def precio_abono(self, precio_abono):
        self.__precio_abono = precio_abono

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, plaza):
        self.__plaza = plaza

    def __str__(self):
        return f"\t\tABONO \n" \
               f"------------------------------\n" \
               f"DNI: {self.dni} \n" \
               f"Nombre Completo: {self.nombre} {self.apellidos} \n" \
               f"Email: {self.email} \n" \
               f"Tipo del Abono: {self.tipo} \n" \
               f"Plaza de parking: {self.plaza.num_plaza} \n" \
               f"Fecha de caducidad: {self.fecha_caducidad} \n" \
               f"Total cobrado: {self.precio_abono} €\n" \
               f"-------------------------------\n"
