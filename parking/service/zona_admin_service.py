from parking.models.cliente_abonado import ClienteAbonado
from datetime import datetime, timedelta
import pickle


class ZonaAdminService:

    def __init__(self, cliente_abonado_service, ticket_service, vehiculo_service):
        self.__cliente_abonado_service = cliente_abonado_service
        self.__ticket_service = ticket_service
        self.__vehiculo_service = vehiculo_service

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

    @property
    def vehiculo_service(self):
        return self.__vehiculo_service

    @vehiculo_service.setter
    def vehiculo_service(self, vehiculo_service):
        self.__vehiculo_service = vehiculo_service

    def dar_de_alta_a_un_cliente_abonado(self, dni, nombre, apellidos, num_tarjeta, tipo, email, vehiculo, plaza):
        if tipo == 1 and not self.cliente_abonado_service.comprobar_dni(dni) and \
                not self.vehiculo_service.comprobar_matricula(vehiculo.matricula):
            cliente_abonado = ClienteAbonado(dni, nombre, apellidos, num_tarjeta, tipo, email, datetime.now(),
                                             datetime.now() + timedelta(days=30), 25, vehiculo, plaza)
            self.cliente_abonado_service.annadir_cliente_abonado(cliente_abonado)
            return True
        elif tipo == 2 and not self.cliente_abonado_service.comprobar_dni(dni) and \
                not self.vehiculo_service.comprobar_matricula(vehiculo.matricula):
            cliente_abonado = ClienteAbonado(dni, nombre, apellidos, num_tarjeta, tipo, email, datetime.now(),
                                             datetime.now() + timedelta(days=30 * 3), 70, vehiculo, plaza)
            self.cliente_abonado_service.annadir_cliente_abonado(cliente_abonado)
            return True
        elif tipo == 3 and not self.cliente_abonado_service.comprobar_dni(dni) and \
                not self.vehiculo_service.comprobar_matricula(vehiculo.matricula):
            cliente_abonado = ClienteAbonado(dni, nombre, apellidos, num_tarjeta, tipo, email, datetime.now(),
                                             datetime.now() + timedelta(days=30 * 6), 130, vehiculo, plaza)
            self.cliente_abonado_service.annadir_cliente_abonado(cliente_abonado)
            return True
        elif tipo == 4 and not self.cliente_abonado_service.comprobar_dni(dni) and \
                not self.vehiculo_service.comprobar_matricula(vehiculo.matricula):
            cliente_abonado = ClienteAbonado(dni, nombre, apellidos, num_tarjeta, tipo, email, datetime.now(),
                                             datetime.now() + timedelta(days=365), 200, vehiculo, plaza)
            self.cliente_abonado_service.annadir_cliente_abonado(cliente_abonado)
            return True
        else:
            return False

    def imprimir_alta_abonado(self, dni):
        cliente_abonado = self.cliente_abonado_service.buscar_cliente_abonado_por_dni(dni)
        return cliente_abonado

    def modificar_datos_cliente_abonado(self, cliente_abonado_a_modificar, nombre, apellidos, num_tarjeta, email):
        cliente_abonado_a_modificar.nombre = nombre
        cliente_abonado_a_modificar.apellidos = apellidos
        cliente_abonado_a_modificar.num_tarjeta = num_tarjeta
        cliente_abonado_a_modificar.email = email
        print(cliente_abonado_a_modificar)

    def renovar_abono_del_cliente(self, tipo, cliente_abonado_a_renovar):
        if tipo == "Mensual":
            cliente_abonado_a_renovar.fecha_caducidad += timedelta(days=30)
            cliente_abonado_a_renovar.precio_abono += 25
            cliente_abonado_a_renovar.tipo = "Mensual"
        elif tipo == "Trimestral":
            cliente_abonado_a_renovar.fecha_caducidad += timedelta(days=90)
            cliente_abonado_a_renovar.precio_abono += 70
            cliente_abonado_a_renovar.tipo = "Trimestral"
        elif tipo == "Semestral":
            cliente_abonado_a_renovar.fecha_caducidad += timedelta(days=180)
            cliente_abonado_a_renovar.precio_abono += 130
            cliente_abonado_a_renovar.tipo = "Semestral"
        elif tipo == "Anual":
            cliente_abonado_a_renovar.fecha_caducidad += timedelta(days=365)
            cliente_abonado_a_renovar.precio_abono += 200
            cliente_abonado_a_renovar.tipo = "Anual"
        return cliente_abonado_a_renovar

    def dar_de_baja_a_un_cliente_abonado(self, cliente_abonado_a_eliminar):
        self.cliente_abonado_service.lista_clientes_abonados.remove(cliente_abonado_a_eliminar)

    def calcular_facturacion_entre_fechas(self, fecha_primera, fecha_segunda):
        suma = 0.0
        for i in self.ticket_service.lista_tickets:
            if i.pago_realizado and fecha_primera <= i.vehiculo.fecha_salida <= fecha_segunda:
                suma += i.calcular_tarifa_a_pagar(i.vehiculo)
        return suma

    def imprimir_tickets_pagados(self, fecha_primera, fecha_segunda):
        resultado = list()
        for i in self.ticket_service.lista_tickets:
            if i.pago_realizado and fecha_primera <= i.vehiculo.fecha_salida <= fecha_segunda:
                resultado.append(i)
        return resultado

    def imprimir_clientes_abonados(self):
        lista_clientes_abonados = self.cliente_abonado_service.buscar_clientes_abonados()
        if len(lista_clientes_abonados) == 0:
            return "No hay ningún cliente abonado en estos momentos"
        else:
            for i in lista_clientes_abonados:
                return i

    def imprimir_caducidad_mes(self, mes):
        resultado = self.cliente_abonado_service.buscar_caducidad_abonos_mes(mes)
        if len(resultado) == 0:
            return "No se ha encontrado ningún abono que caduque en ese mes"
        else:
            for i in resultado:
                return i

    def imprimir_caducidad_diez_dias(self):
        resultado = self.cliente_abonado_service.buscar_caducidad_diez_dias()
        if len(resultado) == 0:
            return "No se ha encontrado ningún abono que caduque en ese mes"
        else:
            for i in resultado:
                print(i)
