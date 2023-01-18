from parking.models.cliente_abonado import ClienteAbonado
from datetime import datetime, timedelta
import pickle


class ZonaAdminService:

    def __init__(self, cliente_abonado_service, ticket_service):
        self.__cliente_abonado_service = cliente_abonado_service
        self.__ticket_service = ticket_service

    @property
    def cliente_abonado_service(self):
        return self.__cliente_abonado_service

    @cliente_abonado_service.setter
    def cliente_abonado_service(self, cliente_abonado_service):
        self.__cliente_abonado_service = cliente_abonado_service

    @property
    def ticket_service(self):
        return self.__ticket_service

    @ticket_service.setter
    def ticket_service(self, ticket_service):
        self.__ticket_service = ticket_service

    def dar_de_alta_a_un_cliente_abonado(self, dni, nombre, apellidos, num_tarjeta, tipo, email, vehiculo, plaza):
        if tipo == 1:
            cliente_abonado = ClienteAbonado(dni, nombre, apellidos, num_tarjeta, tipo, email, datetime.now(),
                                             datetime.now() + timedelta(days=30), 25, vehiculo, plaza)
            self.cliente_abonado_service.annadir_cliente_abonado(cliente_abonado)
        elif tipo == 2:
            cliente_abonado = ClienteAbonado(dni, nombre, apellidos, num_tarjeta, tipo, email, datetime.now(),
                                             datetime.now() + timedelta(days=30 * 3), 70, vehiculo, plaza)
            self.cliente_abonado_service.annadir_cliente_abonado(cliente_abonado)
        elif tipo == 3:
            cliente_abonado = ClienteAbonado(dni, nombre, apellidos, num_tarjeta, tipo, email, datetime.now(),
                                             datetime.now() + timedelta(days=30 * 6), 130, vehiculo, plaza)
            self.cliente_abonado_service.annadir_cliente_abonado(cliente_abonado)
        elif tipo == 4:
            cliente_abonado = ClienteAbonado(dni, nombre, apellidos, num_tarjeta, tipo, email, datetime.now(),
                                             datetime.now() + timedelta(days=365), 200, vehiculo, plaza)
            self.cliente_abonado_service.annadir_cliente_abonado(cliente_abonado)
        return True

    def imprimir_alta_abonado(self, dni):
        cliente_abonado = self.cliente_abonado_service.buscar_cliente_abonado_por_dni(dni)
        return cliente_abonado

    def modificar_datos_cliente_abonado(self, cliente_abonado_a_modificar, nombre, apellidos, num_tarjeta, email):
        cliente_abonado_a_modificar.nombre = nombre
        cliente_abonado_a_modificar.apellidos = apellidos
        cliente_abonado_a_modificar.num_tarjeta = num_tarjeta
        cliente_abonado_a_modificar.email = email
        print(cliente_abonado_a_modificar)

    def renovar_abono_del_cliente(self, cliente_abonado_a_renovar):
        tipo_abono = cliente_abonado_a_renovar.tipo
        if tipo_abono == "Mensual":
            cliente_abonado_a_renovar.fecha_caducidad += timedelta(days=30)
            cliente_abonado_a_renovar.precio_abono += 25
        elif tipo_abono == "Trimestral":
            cliente_abonado_a_renovar.fecha_caducidad += timedelta(days=30 * 3)
            cliente_abonado_a_renovar.precio_abono += 70
        elif tipo_abono == "Semestral":
            cliente_abonado_a_renovar.fecha_caducidad += timedelta(days=30 * 6)
            cliente_abonado_a_renovar.precio_abono += 130
        elif tipo_abono == "Anual":
            cliente_abonado_a_renovar.fecha_caducidad += timedelta(days=365)
            cliente_abonado_a_renovar.precio_abono += 200
        print(cliente_abonado_a_renovar)

    def dar_de_baja_a_un_cliente_abonado(self, cliente_abonado_a_eliminar):
        self.cliente_abonado_service.lista_clientes_abonados.remove(cliente_abonado_a_eliminar)

    def imprimir_facturacion_entre_fechas(self, fecha_primera, fecha_segunda):
        facturacion = self.ticket_service.calcular_facturacion_entre_fechas(fecha_primera, fecha_segunda)

        for i in facturacion:
            return "\nPARKING JLGM \n" \
                  "------------------------------------------------- \n" \
                  f"Matrícula: {i.vehiculo.matricula} \n" \
                  f"Tiempo de estancia:  {i.vehiculo.fecha_salida - i.vehiculo.fecha_deposito} minutos\n" \
                  f"Cobro realizado: {i.calcular_tarifa_a_pagar(i)} \n" \
                  f"-----------------------------------------------\n"

    def convertir_fecha(self, fecha_string):
        return datetime.strptime(fecha_string, '%Y%m%d')

    def imprimir_clientes_abonados(self):
        lista_clientes_abonados = self.cliente_abonado_service.buscar_clientes_abonados()
        for i in lista_clientes_abonados:
            return i

    def imprimir_caducidad_mes(self, mes):
        resultado = self.cliente_abonado_service.buscar_caducidad_abonos_mes(mes)
        for i in resultado:
            return i
    def imprimir_caducidad_diez_dias(self):
        resultado = self.cliente_abonado_service.buscar_caducidad_diez_dias()
        for i in resultado:
            print(i)