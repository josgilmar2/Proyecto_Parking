from parking.models.parking import Parking
from parking.models.turismo import Turismo
from parking.models.ticket import Ticket
from parking.models.plaza import Plaza
from parking.models.admin import Admin
from parking.models.cliente_abonado import ClienteAbonado
from parking.models.motocicleta import Motocicleta
from parking.models.movilidad_reducida import MovilidadReducida
from parking.service.vehiculo_service import VehiculoService
from parking.service.plaza_service import PlazaService
from parking.service.ticket_service import TicketService
from parking.service.parking_service import ParkingService
from parking.service.cliente_abonado_service import ClienteAbonadoService
from parking.service.zona_cliente_service import ZonaClienteService
from parking.service.zona_admin_service import ZonaAdminService

import pickle
from datetime import datetime, timedelta
import random

lista_vehiculos = list()
lista_plazas = list()
lista_tickets = list()
lista_clientes_abonados = list()

admin = Admin("admin", "1234")

t1 = Turismo("1111DDD", datetime.now(), None, None)
t2 = Turismo("2222CCC", datetime(2023, 1, 18, 22, 22, 22), datetime(2023, 1, 19, 13, 45, 46), None)

m1 = Motocicleta("3333GGG", datetime(2023, 1, 19, 12, 34, 23), datetime(2023, 1, 19, 17, 32, 1), None)
m2 = Motocicleta("4444FFF", datetime.now(), None, None)

mv1 = MovilidadReducida("5555HHH", datetime(2023, 1, 19, 8, 12, 2), datetime(2023, 1, 19, 11, 23, 32), None)

p1 = Plaza(7, 123456, True, t1)
p2 = Plaza(23, 567890, True, t2)
p3 = Plaza(59, 345678, True, m1)
p4 = Plaza(63, 234567, True, m2)
p5 = Plaza(75, 456789, True, mv1)

t1.plaza = p1
t2.plaza = p2
m1.plaza = p3
m2.plaza = p4
mv1.plaza = p5

tk1 = Ticket(t1, False)
tk2 = Ticket(t2, True)
tk3 = Ticket(m1, True)
tk4 = Ticket(m2, False)
tk5 = Ticket(mv1, True)

a1 = ClienteAbonado("29535936A", "José Luis", "Gil Martín", "0000-0000-0000-0000", "Mensual",
                    "josgilmar2@gmail.com", datetime.now(), datetime.now() + timedelta(days=30), 25, t1, p1)


lista_vehiculos = [t1, t2, m1, m2, mv1]
lista_plazas = [p1, p2, p3, p4, p5]
lista_tickets = [tk1, tk2, tk3, tk4, tk5]
lista_clientes_abonados = [a1]

fichero_vehiculo = open("data/vehiculos", "wb")
pickle.dump(lista_vehiculos, fichero_vehiculo)
fichero_vehiculo.close()

fichero_plaza = open("data/plazas", "wb")
pickle.dump(lista_vehiculos, fichero_plaza)
fichero_plaza.close()

fichero_ticket = open("data/plazas", "wb")
pickle.dump(lista_tickets, fichero_ticket)
fichero_ticket.close()

fichero_cliente_abonado = open("data/clientes_abonados", "wb")
pickle.dump(lista_clientes_abonados, fichero_cliente_abonado)
fichero_cliente_abonado.close()


parking = Parking(lista_vehiculos, 80, 56, 12, 12)
parking_service = ParkingService(parking)

vehiculo_service = VehiculoService(lista_vehiculos)
plaza_service = PlazaService(lista_plazas)
ticket_service = TicketService(lista_tickets)
cliente_abonado_service = ClienteAbonadoService(lista_clientes_abonados)

zona_cliente_service = ZonaClienteService(parking_service, vehiculo_service, plaza_service, ticket_service)
zona_admin_service = ZonaAdminService(cliente_abonado_service, ticket_service, vehiculo_service)

op = -1
while op != 0:
    print("\nBienvenido al Parking JLGM.\n"
          "---------------------------------\n"
          "Pulsa 1 para entrar como CLIENTE \n"
          "Pulse 2 para ABONARSE \n"
          "Pulse 3 para entrar como ADMINISTRADOR \n"
          "Pulse 0 para salir")
    try:
        op = int(input())
        if op != 1 and op != 2 and op != 3 and op != 0:
            raise ValueError
        else:
            op2 = -1
            if op == 1:
                while op2 != 0:
                    print("Has accedido al menú de CLIENTE \n"
                          "------------------------------------------- \n"
                          "Pulse 1 para depositar un vehículo \n"
                          "Pulse 2 para retirar un vehículo \n"
                          "Pulse 3 para depositar un vehículo como abonado \n"
                          "Pulse 4 para retirar un vehiculo como abonado \n"
                          "Pulse 0 para salir")
                    try:
                        op2 = int(input())
                        if op2 != 1 and op2 != 2 and op2 != 3 and op2 != 4 and op2 != 0:
                            raise ValueError
                        else:
                            if op2 == 1:
                                try:
                                    print("\n¿Qué quiere depositar? \n"
                                          "-------------------------------------\n"
                                          "Pulse 1 para depositar turismo\n"
                                          "Pulse 2 para depositar motocicleta\n"
                                          "Pulse 3 para depositar en movilidad reducida\n"
                                          "Pulse 0 para salir")
                                    op3 = int(input())
                                    if op3 != 1 and op3 != 2 and op3 != 3 and op3 != 0:
                                        raise ValueError
                                    if op3 == 1:
                                        matricula = input("Diga la matrícula de su vehículo: ")
                                        vehiculo = Turismo(matricula, datetime.now(), None, p1)
                                        zona_cliente_service.depositar_vehiculo_normal(vehiculo)
                                    elif op3 == 2:
                                        matricula = input("Diga la matrícula de su vehículo: ")
                                        vehiculo = Motocicleta(matricula,  datetime.now(), None, p1)
                                        zona_cliente_service.depositar_vehiculo_normal(vehiculo)
                                    elif op3 == 3:
                                        matricula = input("Diga la matrícula de su vehículo: ")
                                        vehiculo = MovilidadReducida(matricula, datetime.now(), None, p1)
                                        zona_cliente_service.depositar_vehiculo_normal(vehiculo)
                                except ValueError:
                                    print("ERROR. Tienes que introducir una de las opciones que se piden")
                            elif op2 == 2:
                                matricula = input("Introduzca la matrícula de su vehículo: ")
                                num_plaza = int(input("Introduzca el número de plaza donde ha aparcado: "))
                                pin = int(input("Introduzca el pin que aparecía en el ticket: "))
                                zona_cliente_service.retirar_vehiculo_normal(matricula, num_plaza, pin)
                            elif op2 == 3:
                                dni = input("Introduzca el dni para saber si estás abonado al parking: ")
                                matricula = input("Introduzca la matrícula de su vehículo para saber si está abonado "
                                                  "al parking: ")
                                if cliente_abonado_service.comprobar_cliente_abonado(dni, matricula):
                                    cliente_abonado = cliente_abonado_service.buscar_cliente_abonado_por_dni(dni)
                                    try:
                                        print(f"\nBuenas {cliente_abonado.nombre} {cliente_abonado.apellidos}\n")
                                        pin = int(input("Diga el pin de su abono para depositar su vehículo: "))
                                        print(zona_cliente_service.depositar_vehiculo_abonado(cliente_abonado, pin))
                                    except ValueError:
                                        print("\nERROR. Has introducido incorrectamente el pin\n")
                                else:
                                    print("\nEl dni o la matrícula son incorrectos\n")
                            elif op2 == 4:
                                dni = input("Introduzca el dni para saber si estás abonado al parking: ")
                                matricula = input("Introduzca la matrícula de su vehículo para saber si está abonado "
                                                  "al parking: ")
                                if cliente_abonado_service.comprobar_cliente_abonado(dni, matricula):
                                    cliente_abonado = cliente_abonado_service.buscar_cliente_abonado_por_dni(dni)
                                try:
                                    print(f"\nBuenas {cliente_abonado.nombre} {cliente_abonado.apellidos}\n")
                                    pin = int(input("Diga el pin de su abono para retirar su vehículo: "))
                                    print(zona_cliente_service.retirar_vehiculo_abonado(cliente_abonado, pin))
                                except ValueError:
                                    print("\nERROR. Has introducido incorrectamente el pin\n")
                    except ValueError:
                        print("ERROR. Tienes que introducir una de las opciones que se piden")
            elif op == 2:
                while op2 != 0:
                    print("\nHas accedido al menú de ABONOS \n"
                          "------------------------------------------- \n"
                          "Pulse 1 para darte de alta\n"
                          "Pulse 2 para modificarlo \n"
                          "Pulse 3 para darte de baja \n"
                          "Pulse 0 para salir")
                    try:
                        op2 = int(input())
                        if op2 != 1 and op2 != 2 and op2 != 3 and op2 != 0:
                            raise ValueError
                        else:
                            if op2 == 1:
                                for i in lista_clientes_abonados:
                                    print(i)
                                print("\nPara abonarse, siga las siguientes instrucciones:\n")
                                dni = input("Introduce tu dni: ")
                                nombre = input("Introduce tu nombre: ")
                                apellidos = input("Introduce tu apellidos: ")
                                num_tarjeta = input("Introduce tu número de tarjeta: ")
                                tipo = int(input("\nIntroduce el tipo del abono: \n"
                                                 "-------------------------------\n"
                                                 "Pulse 1 para un abono Mensual\n"
                                                 "Pulse 2 para un abono Trimestral\n"
                                                 "Pulse 3 para un abono Semestral\n"
                                                 "Pulse 4 para un abono Anual\n"))
                                try:
                                    if tipo != 1 and tipo != 2 and tipo != 3 and tipo != 4:
                                        raise ValueError
                                    elif tipo == 1:
                                        tipo_abono = "Mensual"
                                    elif tipo == 2:
                                        tipo_abono = "Trimestral"
                                    elif tipo == 3:
                                        tipo_abono = "Semestral"
                                    elif tipo == 4:
                                        tipo_abono = "Anual"
                                except ValueError:
                                    print("ERROR. Tienes que introducir una de las opciones que se piden")
                                email = input("Introduce tu email: ")
                                matricula = input("Introduce la matrícula del vehículo a estacionar: ")
                                tipo_vehiculo = int(input("\nIndique el tipo de vehículo: \n"
                                                          "Pulse 1 para turismo\n"
                                                          "Pulse 2 para motocicleta\n"
                                                          "Pulse 3 para movilidad reducida\n"))
                                try:
                                    if tipo_vehiculo != 1 and tipo_vehiculo != 2 and tipo_vehiculo != 3:
                                        raise ValueError
                                    elif tipo_vehiculo == 1:
                                        vehiculo_del_abonado = Turismo(matricula, None, None, None)
                                    elif tipo_vehiculo == 2:
                                        vehiculo_del_abonado = Motocicleta(matricula, None, None, None)
                                    elif tipo_vehiculo == 3:
                                        vehiculo_del_abonado = MovilidadReducida(matricula, None, None, None)
                                except ValueError:
                                    print("ERROR. Tienes que introducir una de las opciones que se piden")
                                pin = int(input("Por último, introduzca un pin: "))
                                plaza = Plaza(random.randint(1, parking.plazas_totales), pin, True,
                                              vehiculo_del_abonado)
                                vehiculo_del_abonado.plaza = plaza
                                if zona_admin_service.dar_de_alta_a_un_cliente_abonado(dni, nombre, apellidos,
                                                                                       num_tarjeta, tipo, email,
                                                                                       vehiculo_del_abonado, plaza):
                                    print(zona_admin_service.imprimir_alta_abonado(dni))
                                    print("Usted se ha abonado al Parking JLGM con éxito\n")

                                else:
                                    print("\nNo se ha agregado correctamente como abonado ya que el dni o la "
                                          "matrícula están registradas en el sistema. Inténtelo de nuevo\n")
                            elif op2 == 2:
                                print("\n¿Qué desea modificar de su abono?\n"
                                      "-----------------------------------\n"
                                      "Pulse 1 para modificar sus datos personales\n"
                                      "Pulse 2 para renovar su abono")
                                try:
                                    op3 = int(input())
                                    if op3 != 1 and op3 != 2 and op3 != 0:
                                        raise ValueError
                                    else:
                                        if op3 == 1:
                                            dni = input("Introduce tu dni para poder acceder a tu abono: ")
                                            comprobacion = False
                                            for i in lista_clientes_abonados:
                                                if i.dni == dni:
                                                    cliente_abonado_a_modificar = i
                                                    comprobacion = True
                                            if comprobacion:
                                                nombre = input("\nIntroduzca su nuevo nombre: ")
                                                apellidos = input("Introduzca sus nuevos apellidos: ")
                                                num_tarjeta = input("Introduzca su nuevo número de tarjeta: ")
                                                email = input("Introduzca su nuevo email: ")
                                                zona_admin_service.modificar_datos_cliente_abonado(
                                                    cliente_abonado_a_modificar, nombre, apellidos, num_tarjeta, email)
                                                print("\nSu abono se ha modificado con éxito\n")
                                            else:
                                                print("\nEl dni es incorrecto.\n")
                                        elif op3 == 2:
                                            dni = input("Introduce tu dni para poder acceder a tu abono: ")
                                            comprobacion = False
                                            for i in lista_clientes_abonados:
                                                if i.dni == dni:
                                                    cliente_abonado_a_renovar = i
                                                    comprobacion = True
                                            if comprobacion:
                                                tipo = int(input("\nIntroduce el tipo del abono para renovar el suyo: "
                                                                 "\n"
                                                                 "-------------------------------\n"
                                                                 "Pulse 1 para un abono Mensual\n"
                                                                 "Pulse 2 para un abono Trimestral\n"
                                                                 "Pulse 3 para un abono Semestral\n"
                                                                 "Pulse 4 para un abono Anual\n"))
                                                try:
                                                    if tipo != 1 and tipo != 2 and tipo != 3 and tipo != 4:
                                                        raise ValueError
                                                    elif tipo == 1:
                                                        tipo_abono = "Mensual"
                                                    elif tipo == 2:
                                                        tipo_abono = "Trimestral"
                                                    elif tipo == 3:
                                                        tipo_abono = "Semestral"
                                                    elif tipo == 4:
                                                        tipo_abono = "Anual"
                                                except ValueError:
                                                    print("ERROR. Tienes que introducir una de las opciones que se "
                                                          "piden")
                                                print(zona_admin_service.renovar_abono_del_cliente(tipo_abono, cliente_abonado_a_renovar))
                                                print("\nSu abono se ha modificado con éxito\n")
                                            else:
                                                print("\nEl dni es incorrecto.\n")
                                except ValueError:
                                    print("\nERROR. Tienes que introducir una de las opciones que se piden")
                            elif op2 == 3:
                                dni = input("Introduce tu dni para poder acceder a tu abono: ")
                                comprobacion = False
                                for i in lista_clientes_abonados:
                                    if i.dni == dni:
                                        cliente_abonado_a_eliminar = i
                                        comprobacion = True
                                if comprobacion:
                                    zona_admin_service.dar_de_baja_a_un_cliente_abonado(cliente_abonado_a_eliminar)
                                    print("\nSe ha dado de baja con éxito.\n")
                                else:
                                    print("\nEl dni es incorrecto.\n")
                    except ValueError:
                        print("\nERROR. Tienes que introducir una de las opciones que se piden")
            elif op == 3:
                usuario = input("\nPara entrar como ADMINISTRADOR, primeramente deberá realizar un loguin.\n"
                                "(Las credenciales se encuentran arriba del fichero main.py)\n"
                                "\nPara empezar introduzca su usuario: ")
                contrasenna = input("Ahora, introduzca su contraseña: ")
                if admin.usuario == usuario and admin.contrasenna == contrasenna:
                    print(f"\n¡¡¡CREDENCIALES CORRECTAS!!! Bienvenido {admin.usuario}\n")
                    op2 = -1
                    while op2 != 0:
                        print("\nHas accedido al menú de ADMINISTRADOR \n"
                              "------------------------------------------- \n"
                              "Pulse 1 para ver el estado del parking\n"
                              "Pulse 2 para ver la facturación entre dos fechas \n"
                              "Pulse 3 para consultar a los abonados \n"
                              "Pulse 4 para ver la caducidad de abonos\n"
                              "Pulse 0 para salir")
                        try:
                            op2 = int(input())
                            if op2 != 1 and op2 != 2 and op2 != 3 and op2 != 4:
                                raise ValueError
                            else:
                                if op2 == 1:
                                    print(parking_service.ver_plazas_parking(parking))
                                elif op2 == 2:
                                    print("\n¡¡¡Recuerda la primera fecha debe ser más pequeña que la segunda!!!")
                                    anno_primero = input("Año: ")
                                    mes_primero = input("Mes: ")
                                    dia_primero = input("Día: ")
                                    hora_primera = input("Hora: ")
                                    minutos_primero = input("Minutos: ")
                                    fecha_primera = datetime(int(anno_primero), int(mes_primero), int(dia_primero), int(hora_primera),
                                                             int(minutos_primero))
                                    print("\nIntroduzca la segunda fecha")
                                    anno_segundo = input("Año: ")
                                    mes_segundo = input("Mes: ")
                                    dia_segundo = input("Día: ")
                                    hora_segundo = input("Hora: ")
                                    minutos_segundo = input("Minutos: ")
                                    fecha_segunda = datetime(int(anno_segundo), int(mes_segundo), int(dia_segundo), int(hora_segundo),
                                                             int(minutos_segundo))
                                    for i in zona_admin_service.imprimir_tickets_pagados(fecha_primera, fecha_segunda):
                                        print(i)
                                    print(f"\nEl total recaudado entre la fecha: {fecha_primera} "
                                          f"y la fecha: {fecha_segunda} es de {round(zona_admin_service.calcular_facturacion_entre_fechas(fecha_primera, fecha_segunda), 2)} €")
                                elif op2 == 3:
                                    if len(lista_clientes_abonados) == 0:
                                        print("\nAhora mismo no existe ningún abonado al parking")
                                    else:
                                        for i in lista_clientes_abonados:
                                            print(i)
                                elif op2 == 4:
                                    print("\n¿Qúe desea consultar?\n"
                                          "-----------------------------------------------------\n"
                                          "Pulse 1 para consultar la caducidad de los abonos de un mes concreto\n"
                                          "Pulse 2 para consultar los abonos que caducan en los siguientes 10 días\n"
                                          "Pulse 0 para salir")
                                    try:
                                        op3 = int(input())
                                        if op3 != 1 and op3 != 2 and op3 != 0:
                                            raise ValueError
                                        else:
                                            if op3 == 1:
                                                mes = int(input("\nIntroduce el mes de caducidad: "))
                                                print()
                                                print(zona_admin_service.imprimir_caducidad_mes(mes))
                                            elif op3 == 2:
                                                print(zona_admin_service.imprimir_caducidad_diez_dias())
                                    except ValueError:
                                        print("\nERROR. Tienes que introducir una de las opciones que se piden")
                        except ValueError:
                            print("\nERROR. Tienes que introducir una de las opciones que se piden")
                else:
                    print("\n¡¡¡CREDENCIALES INCORRECTAS!!! Inténtelo de nuevo")
            elif op == 0:
                break
    except ValueError:
        print("\nERROR. Tienes que introducir una de las opciones que se piden")
