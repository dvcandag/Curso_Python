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
print('Saldo luego de depositar S/ 2220---->', cliente1.saldo)
cliente1.extraer(1000)
print('Saldo luego de extraer S/ 120---->', cliente1.saldo)
