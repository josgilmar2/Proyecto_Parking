import pickle
from datetime import datetime, timedelta

class ClienteAbonadoService:

    def __init__(self, lista_clientes_abonados):
        self.__lista_clientes_abonados = lista_clientes_abonados

    @property
    def lista_clientes_abonados(self):
        return self.__lista_clientes_abonados

    @lista_clientes_abonados.setter
    def lista_clientes_abonados(self, lista_clientes_abonados):
        self.__lista_clientes_abonados = lista_clientes_abonados

    def buscar_cliente_abonado_por_dni(self, dni):
        for i in self.lista_clientes_abonados:
            if i.dni == dni:
                return i
        return None

    def comprobar_cliente_abonado(self, dni, matricula):
        cliente_abonado = self.buscar_cliente_abonado_por_dni(dni)
        try:
            if cliente_abonado.vehiculo.matricula == matricula:
                return True
            else:
                return False
        except AttributeError:
            return False

    def annadir_cliente_abonado(self, cliente_abonado):
        self.lista_clientes_abonados.append(cliente_abonado)
        fichero_cliente_abonado = open("./data/clientes_abonados", "wb")
        pickle.dump(self.lista_clientes_abonados, fichero_cliente_abonado)
        fichero_cliente_abonado.close()

    def buscar_clientes_abonados(self):
        result = list()
        for i in self.lista_clientes_abonados:
            result.append(i)
        return result

    def buscar_caducidad_abonos_mes(self, mes):
        resultado = list()
        for i in self.lista_clientes_abonados:
            if int(i.fecha_caducidad.month) == mes:
                resultado.append(i)
        return resultado

    def buscar_caducidad_diez_dias(self):
        resultado = list()
        fecha_final = datetime.now() + timedelta(days=10)
        for i in self.lista_clientes_abonados:
            if datetime.now() < i.fecha_caducidad < fecha_final:
                resultado.append(i)
        return resultado

    def comprobar_dni(self, dni):
        for i in self.lista_clientes_abonados:
            if i.dni == dni:
                return True
        return False
