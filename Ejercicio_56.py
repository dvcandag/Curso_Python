"""
Ejercicio 56:
Desarrollar una clase llamada "Cliente", diseñada para representar a un cliente de un banco y 
permitir operaciones básicas de gestión de saldo, los saldos deben salir en moneda peruana. La clase 
debe tener los siguientes atributos y métodos:

Atributos:
a) nombre: Almacena el nombre del cliente.
b) deposito: Guarda el saldo actual del cliente, inicialmente en 0.

Métodos:
a) __init__(self, nombre): Un constructor que inicializa el nombre del cliente y su saldo.
b) imprimir(self): Un método que imprime el nombre y el saldo del cliente.
c) depositar(self, monto): Permite al cliente depositar una cantidad específica.
d) extraer(self, monto): Posibilita al cliente extraer una cantidad específica

Proporcionar comentarios explicativos. Tu solución debe entregarse en un archivo .py
"""

# Definición de la clase Cliente
class Cliente:
    def __init__(self, nombre):
        # Inicialización de los atributos nombre y deposito
        self.nombre = nombre
        self.deposito = 0
    
    def imprimir(self):
        # Método para imprimir el nombre y el saldo del cliente en formato de moneda peruana
        print(self.nombre)
        print(f'S/ {self.deposito:,.2f}')  # Utiliza f-string para formatear el saldo como moneda peruana
    
    def depositar(self, monto):
        # Método para depositar una cantidad específica en la cuenta del cliente
        self.deposito += monto
    
    def extraer(self, monto):
        # Método para extraer una cantidad específica de la cuenta del cliente
        self.deposito -= monto

# Creación de un cliente llamado "Vitto Andagua"
cliente1 = Cliente('Vitto Andagua')

# Imprimir estado inicial del cliente
cliente1.imprimir()

# Depositar 100,000 soles en la cuenta del cliente
cliente1.depositar(100000)
print('Estado luego de depositar 100,000 soles')
cliente1.imprimir()

# Extraer 40,000 soles de la cuenta del cliente
cliente1.extraer(40000)
print('Estado luego de extraer 40,000 soles')
cliente1.imprimir()
