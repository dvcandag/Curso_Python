"""Ejercicio 52: Desarrolla un programa en Python que simule una apuesta entre dos jugadores, Juan y Ana. 
El programa debe realizar las siguientes acciones:

1.- Ingreso de números:
    a.- Cada jugador debe ingresar un número de 1 a 100 para participar en la apuesta.
    
2.- Sorteo del número ganador:
    a.- Se simulará el sorteo de un número aleatorio que será el número ganador de la apuesta.
    
3.- Comparación de números:
    a.- Se comparará el número elegido por cada jugador con el número ganador sorteado.
    b.- Si el número ganador es primo, Ana automáticamente será declarada como ganadora.
    
4.- Anuncio de ganadores:
    a.- Ana siempre sea declarada ganadora si selecciona un número primo o si Juan 
    selecciona un número cercano a -3 o +2 del número primo elegido por Ana"""

import random

class JugadorTeApuesto:
    def __init__(self, nombre):
        self.nombre = nombre

    def seleccionar_numero(self):
        self.numero = int(input(f"{self.nombre}, por favor, elige un número entre 1 y 100 para la apuesta: "))

    def verificar_ganador(self, num_sorteado):
        if self.nombre == "Ana":
            if self.es_primo(self.numero):
                return True
            elif num_sorteado - 3 <= self.numero <= num_sorteado + 2:
                print(f'{self.nombre}, ¡estuviste cerca! ha ganado')
                return True
        elif self.nombre == "Juan":
            if num_sorteado - 3 <= self.numero <= num_sorteado + 2:
                return False
        return False

    def es_primo(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

class Sorteador:
    def __init__(self):
        self.numero_sorteado = -1

    def sortear_numero(self):
        self.numero_sorteado = random.randint(1, 100)

# Bloque principal
jugador1 = JugadorTeApuesto("Juan")
jugador1.seleccionar_numero()
jugador2 = JugadorTeApuesto("Ana")
jugador2.seleccionar_numero()
sorteador = Sorteador()

if jugador1.verificar_ganador(sorteador.numero_sorteado):
    print(f'¡{jugador1.nombre} ha ganado!')
else:
    print(f'{jugador1.nombre}, ¡No ganaste!')

if jugador2.verificar_ganador(sorteador.numero_sorteado):
    print(f'¡{jugador2.nombre} ha ganado!')
    print('Número sorteado por el TeApuesto:', jugador2.numero)
else:
    print(f'{jugador2.nombre}, ¡No ganaste!')
