import pickle


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
        fichero_cliente_abonado = open("./data/clientes_abonados", "rb")
        datos_cliente_abonado = pickle.load(fichero_cliente_abonado)
        for i in datos_cliente_abonado:
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

    def editar_cliente_abonado(self, cliente_abonado):
        cliente_abonado_a_editar = self.buscar_cliente_abonado_por_dni(cliente_abonado.dni)
