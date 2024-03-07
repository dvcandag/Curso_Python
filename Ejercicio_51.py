
"""Desarrolla un programa en Python que modele el comportamiento de un cliente bancario. 
Utiliza la clase Cliente para representar a un cliente, con el objetivo de realizar 
operaciones bancarias simples como depósitos y retiros.

1.- Crea una instancia de la clase Cliente llamada cliente1 con el nombre "Diego" y un saldo inicial de 1200.
2.- Imprime el nombre del cliente y su saldo actual.
3.- Deposita 120 unidades de dinero en la cuenta del cliente.
4.- Imprime el saldo actual después de realizar el depósito.
5.- Extrae 1000 unidades de dinero de la cuenta del cliente.
6.- Imprime el saldo actual después de realizar la extracción.
7.- El programa debe reflejar estas acciones utilizando la clase Cliente para manejar
la información del cliente y realizar las operaciones bancarias necesarias"""


class Cliente:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def depositar(self, dinero):
        self.saldo += dinero

    def extraer(self, dinero):
        self.saldo -= dinero

cliente1 = Cliente('diego', 1200)
print('Nombre del cliente:', cliente1.nombre)
print('Saldo actual:', cliente1.saldo)
cliente1.depositar(120)
print('Saldo luego de depositar S/ 425---->', cliente1.saldo)
cliente1.extraer(1000)
print('Saldo luego de extraer S/ 300---->', cliente1.saldo)
