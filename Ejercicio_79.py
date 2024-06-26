"""
Ejercicio 79: Año olímpico

Desarrolla un programa en Python que determine si un año ingresado por el usuario es un año olímpico o no. Un año es 
considerado olímpico si es divisible por 4, excepto aquellos que son divisibles por 100 pero no por 400. El programa 
debe solicitar al usuario que ingrese un año y luego indicar si ese año es un año olímpico o no. Asegúrate de manejar 
correctamente situaciones donde se ingresen valores no válidos para el año.
"""
# SOLUCIÓN

def es_año_olímpico(año):
    # Comprobamos si el año es divisible por 4 y no es divisible por 100, o si es divisible por 400
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

def main():
    try:
        # Solicitamos al usuario que ingrese un año
        año = int(input("Ingrese un año para verificar si es un año olímpico: "))

        # Verificamos si el año ingresado es un año olímpico o no
        if es_año_olímpico(año):
            print(f"{año} es un año olímpico.")
        else:
            print(f"{año} no es un año olímpico.")
    except ValueError:
        print("Error: Ingrese un año válido.")

# Verificamos si este archivo es el punto de entrada principal del programa
if __name__ == "__main__":
    main()
