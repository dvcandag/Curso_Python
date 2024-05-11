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
            
def ingresar_edades(num_personas):
    """
    Solicita al usuario que ingrese las edades de las personas una por una.
    """
    edades = []
    for i in range(num_personas):
        while True:
            try:
                edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
                if edad < 0:
                    print("Por favor, ingrese una edad válida (mayor o igual a cero).")
                else:
                    edades.append(edad)
                    break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
    return edades

def analizar_edades(edades):
    """
    Determinamos la edad mínima, la edad máxima y el promedio de las edades registradas.
    """
    if len(edades) == 0:
        return None, None, None
    edad_minima = min(edades)
    edad_maxima = max(edades)
    promedio_edades = sum(edades) / len(edades)
    return edad_minima, edad_maxima, promedio_edades

def presentar_resultados(edad_minima, edad_maxima, promedio_edades):
    """
    Imprime en pantalla la edad mínima, la edad máxima y el promedio de las edades registradas.
    """
    print("\nResultados del registro de edades:")
    print(f"Edad mínima registrada: {edad_minima}")
    print(f"Edad máxima registrada: {edad_maxima}")
    print(f"Promedio de edades registradas: {promedio_edades}")
    
def programa_registro_edades():
    """
    Codificación de la función principal del programa.
    """
    print("Bienvenido al programa de registro de edades.")
    num_personas = ingresar_numero_personas()
    edades = ingresar_edades(num_personas)
    edad_minima, edad_maxima, promedio_edades = analizar_edades(edades)
    presentar_resultados(edad_minima, edad_maxima, promedio_edades)
