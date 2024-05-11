"""
Ejercicio 77: Registro de Edades

Escribe un programa en Python que realice las siguientes tareas:

1.- Entrada de datos: El programa debe permitir al usuario ingresar el número de personas cuyas edades se registrarán.
2.- Registro de edades: Luego, el programa debe solicitar al usuario que ingrese las edades de las personas una por una.
3.- Análisis de edades: Después de registrar todas las edades, el programa debe determinar la edad mínima, la edad máxima 
    y el promedio de las edades registradas.
4.- Presentación de resultados: Finalmente, el programa debe imprimir en pantalla la edad mínima, la edad máxima y el promedio 
    de las edades registradas.
    
"""

#SOLUCIÓN

def ingresar_numero_personas():
    """
    Solicita al usuario ingresar el número de personas cuyas edades se registrarán.
    """
    while True:
        try:
            num_personas = int(input("Ingrese el número de personas: "))
            if num_personas <= 0:
                print("Por favor, ingrese un número entero positivo.")
            else:
                return num_personas
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")