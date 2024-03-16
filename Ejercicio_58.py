"""
Ejercicio 58:
Desarrollar programa en Python que registre los depósitos realizados por diferentes clientes en un banco. 
El programa debe permitir ingresar el número de cliente y el monto depositado. Si un cliente ha depositado 
más de dos veces, el programa debe mostrar un aviso. Al finalizar, el programa debe mostrar la cantidad total 
de depósitos realizados y el total del monto depositado por todos los clientes. Además, debe indicar 
cuál cliente ha realizado más depósitos.

Instrucciones:
1.- Solicita al usuario ingresar el número de cliente (entero mayor que 0) y el monto a depositar (entero mayor o 
    igual que 0). El ingreso de datos finaliza cuando se ingresa el número de cliente 0.
2.- Si un cliente ha depositado más de dos veces, muestra "Aviso: Este cliente ha depositado más de dos veces."
3.- Al finalizar, muestra la cantidad total de depósitos realizados y el monto total depositado por todos los clientes.
4.- Además, indica qué cliente ha realizado más depósitos.

"""
#SOLUCION:
depositos = {}
while True:
    nro = int(input('Ingrese nro de cliente (0 para finalizar): '))
    if nro == 0:
        break
    monto = int(input('Ingrese monto a depositar: '))
    
    if nro in depositos:
        depositos[nro]['cantidad'] += 1  # Incrementar el contador de depósitos para el cliente
        depositos[nro]['monto_total'] += monto  # Sumar el monto depositado
    else:
        depositos[nro] = {'cantidad': 1, 'monto_total': monto}  # Iniciar el contador de depósitos y el monto total para el cliente

cantidad_depositos = sum(cliente['cantidad'] for cliente in depositos.values())
suma_total = sum(cliente['monto_total'] for cliente in depositos.values())

print('Cantidad de depósitos:', cantidad_depositos)
print('Total depositado por todos los clientes:', suma_total)

# Encontrar al cliente que ha depositado más veces
cliente_mas_depositos = max(depositos, key=lambda x: depositos[x]['cantidad'])
print('Cliente que ha depositado más veces:', cliente_mas_depositos, 'con', depositos[cliente_mas_depositos]['cantidad'], 'depósitos.')


