"""
Ejercicio 78: Tipo de triángulo
Escribe un programa en Python que determine el tipo de triángulo basado en la longitud de sus lados. El programa debe 
solicitar al usuario que ingrese la longitud de los tres lados del triángulo y luego determinar si el triángulo es equilátero 
(todos los lados iguales), isósceles (dos lados iguales) o escaleno (todos los lados diferentes). El programa debe manejar 
correctamente situaciones donde se ingresen valores no válidos para los lados del triángulo.
"""

#SOLUCIÓN

# Definimos una función para determinar el tipo de triángulo
def tipo_triangulo(a, b, c):
    # Comprobamos si todos los lados son iguales (equilátero)
    if a == b == c:
        return "equilátero"
    # Comprobamos si al menos dos lados son iguales (isósceles)
    elif a == b or a == c or b == c:
        return "isósceles"
    # Si no se cumple ninguna de las condiciones anteriores, el triángulo es escaleno
    else:
        return "escaleno"

