"""
Ejercicio 71: clase - denominada "Rectangulo"

Crear una clase en Python denominada "Rectangulo" que tenga atributos de base y altura, 
y que incluya un método para calcular y devolver el área del rectángulo.

Incluir comentarios para explicar el funcionamiento del código.
El código de su solución "El área del rectángulo debe resultar ser 15" y debe estar contenido en un archivo .py que sea ejecutable.

"""

# SOLUCIÓN

# Definición de la clase Rectangulo
class Rectangulo:
    def __init__(self, base, altura):
        """
        Constructor de la clase Rectangulo.

        Args:
            base (float): La medida de la base del rectángulo.
            altura (float): La medida de la altura del rectángulo.
        """
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """
        Método para calcular el área del rectángulo.

        Returns:
            float: El área del rectángulo.
        """
        return self.base * self.altura

# Crear un objeto de la clase Rectangulo con base 5 y altura 3
area = Rectangulo(5, 3).calcular_area()

# Imprimir el área del rectángulo directamente
print("El área del rectángulo es:", area)
