from parking.models.parking import Parking
from parking.service.parking_service import ParkingService

lista_turismos=[]
lista_motocicletas=[]
lista_movilidad_reducida=[]

parking = Parking(lista_turismos, lista_motocicletas, lista_movilidad_reducida)
parking_service = ParkingService(parking)

print("Bienvenido al Parking JLGM.\n")

parking_service.repartir_plazas()

op = -1
while op != 0:
    print("Pulsa 1 para entrar como CLIENTE \n"
          "Pulse 2 para ABONARSE \n"
          "Pulse 3 para entrar como ADMINISTRADOR \n"
          "Pulse 0 para salir")
    op = int(input())
    try:
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
                    op2 = int(input())
                    try:
                        if op2 != 1 and op2 != 2 and op2 != 3 and op2 != 4 and op2 != 0:
                            raise ValueError
                        else:

                            if op2 == 1:
                                try:
                                    parking_service.ver_plazas_libres_normales()
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
                                        print("Introduce la matrícula: ")
                                        if parking_service.depositar_turismo(str(input())):
                                            print("Se ha depositado el turismo con éxito")
                                        else:
                                            print("ERROR. No se ha depositado correctamente el turismo porque no hay "
                                                  "más plazas")
                                    elif op3 == 2:
                                        if parking_service.depositar_motocicleta(str(input())):
                                            print("Se ha depositado la motocicleta con éxito")
                                        else:
                                            print("ERROR. No se ha depositado correctamente la motocicleta porque no "
                                                  "hay más plazas")
                                    elif op3 == 3:
                                        if parking_service.depositar_movilidad_reducida(str(input())):
                                            print("Se ha depositado la motocicleta con éxito")
                                        else:
                                            print(
                                                "ERROR. No se ha depositado correctamente la motocicleta porque no "
                                                "hay más plazas")
                                    elif op3 == 0:
                                        break
                                except ValueError:
                                    print("ERROR. TIenes que introducir una de las opciones que se piden")
                            elif op2 == 2:

                                break
                            elif op2 == 3:
                                break
                            elif op2 == 4:
                                break
                            elif op2 == 0:
                                break
                    except ValueError:
                        print("ERROR. Tienes que introducir una de las opciones que se piden")
            elif op == 2:
                break
            elif op == 3:
                break
            elif op == 0:
                break
    except ValueError:
        print("ERROR. Tienes que introducir una de las opciones que se piden")
