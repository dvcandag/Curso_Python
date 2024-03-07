"""Ejercicio 52: desarrolla un programa en Python que simule apuesta entre dos jugadores, Juan y Ana. 
El programa debe realizar las siguientes acciones:

1.- Ingreso de números:
    a.- Cada jugador debe ingresar un número entre 1 y 10 para participar en la apuesta.
    
2.- Sorteo del número ganador:
    a.- Se debe simular el sorteo de un número aleatorio entre 1 y 10 que será el número ganador de la apuesta.
    
3.- Comparación de números:
    a.- Se debe comparar el número elegido por cada jugador con el número ganador sorteado.
    
4.- Anuncio de ganadores:
    a.- Se debe anunciar si alguno de los jugadores ha ganado la apuesta o si ninguno ha acertado el número ganador."""
    
    
import random

class JugadorTeApuesto:
    def __init__(self, nombre):
        self.nombre = nombre

    def seleccionar_numero(self):
        self.numero = int(input("¿Cuál es tu número para la apuesta, " + self.nombre + "? "))

    def verificar_ganador(self, num_sorteado):
        return self.numero == num_sorteado

class Bolillero:
    def __init__(self):
        self.numero_sorteado = -1

    def sortear_numero(self):
        self.numero_sorteado = random.randint(1, 10)

# Bloque principal
jugador1 = JugadorTeApuesto("Juan")
jugador1.seleccionar_numero()
jugador2 = JugadorTeApuesto("Ana")
jugador2.seleccionar_numero()
sorteador = Bolillero()
sorteador.sortear_numero()

print('Número sorteado:', sorteador.numero_sorteado)
print(f'{jugador1.nombre} eligió el número {jugador1.numero}')
print(f'{jugador2.nombre} eligió el número {jugador2.numero}')

if jugador1.verificar_ganador(sorteador.numero_sorteado):
    print(f'¡{jugador1.nombre} ha ganado!')
if jugador2.verificar_ganador(sorteador.numero_sorteado):
    print(f'¡{jugador2.nombre} ha ganado!')
