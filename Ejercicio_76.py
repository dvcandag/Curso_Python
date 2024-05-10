"""
Ejercicio 76: Programa de cálculo de edades

Escribe un programa en Python que realice las siguientes tareas:

1.- Entrada de datos: El programa debe solicitar al usuario que ingrese el año actual.
2.- Registro de personas: Luego, el programa debe permitir al usuario ingresar el nombre y el año de nacimiento 
    de tres personas diferentes.
3.- Cálculo de edades: Para cada persona registrada, el programa debe calcular la edad que cumplirá durante el año actual.
4.- Presentación de resultados: Finalmente, el programa debe imprimir en pantalla el nombre de cada persona junto con la 
    edad que cumplirá durante el año en curso.

Instrucciones Adicionales:

1.- Asegúrate de que el programa maneje correctamente las entradas del usuario, proporcionando mensajes de error claros 
    en caso de entrada inválida.
2.- Fomenta la modularidad en el diseño de tu programa. Considera cómo dividir las tareas en funciones más pequeñas para facilitar 
    la comprensión y el mantenimiento del código.
3.- Piensa en casos de prueba adicionales que podrían ayudarte a verificar la corrección y robustez de tu programa. Esto podría 
    incluir situaciones como años negativos, nombres con caracteres especiales, etc.
    
"""

# SOLUCIÓN

def solicitar_año_actual():
    while True:
        try:
            # Solicita al usuario que ingrese el año actual
            año_actual = int(input("Por favor, ingresa el año actual: "))
            # Verifica si el año ingresado es válido (positivo)
            if año_actual > 0:
                return año_actual
            else:
                print("Por favor, ingresa un año válido.")
        except ValueError:
            # Maneja la excepción en caso de que el usuario ingrese un valor no numérico
            print("Por favor, ingresa un año válido.")
            
 