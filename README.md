# Proyecto_Parking

<p align="center">
  <img src="https://img.shields.io/badge/STATUS-FINISH-red" alt="Status del proyecto"/>
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-v3.10-blue" alt="Versión java" /></a>
  <img src="https://img.shields.io/badge/release%20date-january-yellowgreen" alt="Lanzamiento del proyecto" />
  <img src="https://img.shields.io/badge/license-MIT-brightgreen" alt="Licencia" />
</p>

## Descripción
**Proyecto_Parking** es una aplicación desarrolada con Python 3.10 que nos permite gestionar un parking dividido en una zona cliente, una zona para abonarse y una zona para administrar.

## Autor
#### José Luis Gil Martín

### Entidades

* #### ClienteAbonado
  - ClienteAbonado (model)
  - ClienteAbonadoService
  - ZonaCLienteService: clase donde se controlan los métodos de la zona cliente

* #### Vehiculo
  - Vehiculo (model)
  - VehiculoService
  - Clase padre de Turismo, Motocicleta y MovilidadReducida

* #### Plaza
  - Plaza (model)
  - PlazaService

* #### Ticket
  - Ticket (model)
  - TicketService

* #### Admin
  - Admin (Model)
  - ZonaAdminService: clase donde se controlan los métodos de la zona admin y de la zona para abonarse


### Funcionalidades de la ZonaCliente

1. Depositar un vehículo
2. Retirar un vehículo
3. Depositar un vehículo de un abonado
4. Retirar el vehículo de un abonado

### Funcionalidades para Abonarse

1. Darse de alta
2. Modificar el abono (datos personales o renovación)
3. Darse de baja

### Funcionalidades de la ZonaAdmin

1. Ver el estado del parking
2. Ver la facturación realizada entre dos fechas
3. Consultar los abonados inscritos al parking
4. Ver la caducidad de los abonos (mes concreto o en los próximos 10 días)

## Arrancar el proyecto

* Descargar PyCharm Community Edition
* Descargar Python v 3.10
* Configurar dentro de PyCharm la configuración para que el proyecto arranque dentro del fichero main.py