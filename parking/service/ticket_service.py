import pickle
from parking.models.ticket import Ticket


class TicketService:

    def __init__(self, lista_tickets):
        self.__lista_tickets = lista_tickets

    @property
    def lista_tickets(self):
        return self.__lista_tickets

    @lista_tickets.setter
    def lista_tickets(self, lista_tickets):
        self.__lista_tickets = lista_tickets

    def crear_ticket_llegada(self, vehiculo):
        ticket = Ticket(vehiculo, False)
        self.lista_tickets.append(ticket)
        fichero_ticket = open("./data/tickets", "wb")
        pickle.dump(self.lista_tickets, fichero_ticket)
        fichero_ticket.close()
        print("\nSe está imprimiendo su ticket. Sea paciente\n")
        print(ticket)

    def crear_ticket_salida(self, vehiculo):
        ticket = Ticket(vehiculo, True)
        self.lista_tickets.append(ticket)
        fichero_ticket = open("./data/tickets", "wb")
        pickle.dump(self.lista_tickets, fichero_ticket)
        fichero_ticket.close()
        print("\nSe está imprimiendo su ticket. Sea paciente\n")
        print(ticket)

    def buscar_tickets_pagados(self):
        lista_tickets = list()
        for i in self.lista_tickets:
            if i.pago_realizado:
                lista_tickets.append(i)
        return lista_tickets

    def calcular_facturacion_entre_fechas(self, fecha_primera, fecha_segunda):
        lista_ticket_pagados = self.buscar_tickets_pagados()
        resultado = list()
        for i in lista_ticket_pagados:
            if fecha_primera <= i.vehiculo.fecha_salida <= fecha_segunda:
                resultado.append(i)
        return resultado
