"""
Ejercicio 69: Generación de subconjuntos

Desarrollar una clase en Python que genere todos los posibles subconjuntos únicos de un conjunto de números enteros distintos.
1.- Entrada: [4, 5, 6]
2.- Salida: [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

Incluir comentarios para explicar el funcionamiento del código.
El código de ejemplo proporcionado en "Entrada" debe estar contenido en un archivo .py que sea ejecutable,
mostrando los subconjuntos generados.
"""

# SOLUCIÓN

class Subconjuntos:
    def generar_subconjuntos(self, conjunto):
        """
        Genera todos los posibles subconjuntos únicos de un conjunto de números enteros distintos.

        :param conjunto: La lista de números enteros distintos.
        :return: Una lista de todos los subconjuntos únicos.
        """
        resultado = [[]]  # Inicializamos con el conjunto vacío como primer subconjunto
        
        for elemento in conjunto:
            # Generamos nuevos subconjuntos agregando el elemento a cada subconjunto existente
            nuevos_subconjuntos = [subconjunto + [elemento] for subconjunto in resultado]
            # Agregamos los nuevos subconjuntos a la lista de resultado
            resultado.extend(nuevos_subconjuntos)
        
        return resultado

# Conjunto de entrada
conjunto = [4, 5, 6]

# Creamos una instancia de la clase Subconjuntos
generador = Subconjuntos()

# Generamos los subconjuntos
subconjuntos = generador.generar_subconjuntos(conjunto)

# Mostramos la salida requerida
print("Salida:", subconjuntos)
