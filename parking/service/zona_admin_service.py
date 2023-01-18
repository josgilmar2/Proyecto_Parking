from parking.models.cliente_abonado import ClienteAbonado
from datetime import datetime, timedelta
import pickle

class ZonaAdminService:

    def __init__(self, cliente_abonado_service):
        self.__cliente_abonado_service = cliente_abonado_service

    @property
    def cliente_abonado_service(self):
        return self.__cliente_abonado_service

    @cliente_abonado_service.setter
    def cliente_abonado_service(self, cliente_abonado_service):
        self.__cliente_abonado_service = cliente_abonado_service

    def dar_de_alta_a_un_cliente_abonado(self, dni, nombre, apellidos, num_tarjeta, tipo, email, vehiculo, plaza):
        if tipo == 1:
            cliente_abonado = ClienteAbonado(dni, nombre, apellidos, num_tarjeta, tipo, email, datetime.now(),
                                             datetime.now() + timedelta(days=30), vehiculo, plaza)
            self.cliente_abonado_service.annadir_cliente_abonado(cliente_abonado)
            return True
        elif tipo == 2:
            cliente_abonado = ClienteAbonado(dni, nombre, apellidos, num_tarjeta, tipo, email, datetime.now(),
                                             datetime.now() + timedelta(days=30 * 3), vehiculo, plaza)
            self.cliente_abonado_service.annadir_cliente_abonado(cliente_abonado)
            return True
        elif tipo == 3:
            cliente_abonado = ClienteAbonado(dni, nombre, apellidos, num_tarjeta, tipo, email, datetime.now(),
                                             datetime.now() + timedelta(days=30 * 6), vehiculo, plaza)
            self.cliente_abonado_service.annadir_cliente_abonado(cliente_abonado)
            return True
        elif tipo == 4:
            cliente_abonado = ClienteAbonado(dni, nombre, apellidos, num_tarjeta, tipo, email, datetime.now(),
                                             datetime.now() + timedelta(days=365), vehiculo, plaza)
            self.cliente_abonado_service.annadir_cliente_abonado(cliente_abonado)
            return True
        return False

    def imprimir_alta_abonado(self, dni, nombre, apellidos, num_tarjeta, tipo, email, vehiculo, plaza):
        if self.dar_de_alta_a_un_cliente_abonado(dni, nombre, apellidos, num_tarjeta, tipo, email, vehiculo, plaza):
            cliente_abonado = self.cliente_abonado_service.buscar_cliente_abonado_por_dni(dni)
            return cliente_abonado

    def modificar_datos_cliente_abonado(self, dni, nombre, apellidos, num_tarjeta, email):
        fichero_cliente_abonado = open("./data/clientes_abonados", "rb")
        datos_cliente_abonado = pickle.load(fichero_cliente_abonado)
        for i in datos_cliente_abonado:
            if i.dni == dni:
                i.nombre = nombre
                i.apellidos = apellidos
                i.num_tarjeta = num_tarjeta
                i.email = email
                return i
        return None

    def renovar_abono_del_cliente(self, cliente_abonado_a_renovar):
        tipo_abono = cliente_abonado_a_renovar.tipo
        if tipo_abono == "Mensual":
            cliente_abonado_a_renovar.fecha_cancelacion += timedelta(days=30)
        elif tipo_abono == "Trimestral":
            cliente_abonado_a_renovar.fecha_cancelacion += timedelta(days=30 * 3)
        elif tipo_abono == "Semestral":
            cliente_abonado_a_renovar.fecha_cancelacion += timedelta(days=30 * 6)
        elif tipo_abono == "Anual":
            cliente_abonado_a_renovar.fecha_cancelacion += timedelta(days=365)
        return cliente_abonado_a_renovar