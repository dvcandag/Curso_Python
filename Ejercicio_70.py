"""
Ejercicio 70: clase - identificación de un par de elementos

Crear una clase en Python que identifique un par de elementos (sus índices) dentro de una matriz dada, 
cuya suma sea igual a un número objetivo especificado.


Incluir comentarios para explicar el funcionamiento del código.
El código de su ejemplo proporcionado debe estar contenido en un archivo .py que sea ejecutable.
"""


#SOLUCIÓN

# Definición de la clase ParDeElementos
class ParDeElementos:
    def __init__(self, matriz):
        """
        Constructor de la clase ParDeElementos.

        Args:
            matriz (list): La matriz en la que se buscarán los pares de elementos.
        """
        self.matriz = matriz

    def encontrar_par_suma(self, objetivo):
        """
        Método para encontrar un par de elementos cuya suma sea igual al objetivo.

        Args:
            objetivo (int): El número objetivo.

        Returns:
            list or None: Una lista con los índices de los pares de elementos cuya suma sea igual al objetivo,
                          o None si no se encuentra ningún par.
        """
        # Se crea un diccionario para almacenar los elementos ya visitados junto con sus índices.
        hash_map = {}

        # Se recorre la matriz para buscar el par de elementos.
        for i, fila in enumerate(self.matriz):
            for j, elemento in enumerate(fila):
                # Se calcula el complemento necesario para alcanzar el objetivo.
                complemento = objetivo - elemento
                # Si el complemento se encuentra en el hash_map, se devuelve el par de índices.
                if complemento in hash_map:
                    return [(hash_map[complemento], (i, j))]
                # Se guarda el elemento actual junto con su índice en el hash_map.
                hash_map[elemento] = (i, j)

        # Si no se encuentra ningún par, se devuelve None.
        return None

# Ejemplo 
matriz_ejemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
objetivo_ejemplo = 10

# Se instancia la clase ParDeElementos con la matriz de ejemplo.
par_elementos = ParDeElementos(matriz_ejemplo)
# Se busca un par de elementos cuya suma sea igual al objetivo.
resultado = par_elementos.encontrar_par_suma(objetivo_ejemplo)
# Se imprime el resultado.
print(resultado)


