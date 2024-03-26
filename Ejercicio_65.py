"""
Ejercicio 64: Declaraciones condicionales y elif

Desarrolla un programa que, gradualmente, permita comprender el funcionamiento de las declaraciones 
condicionales if, elif (abreviatura de "else if") y else en Python, facilitando así la comprensión 
de las estructuras de control de flujo en la programación informática.

Agregar comentarios explicativos. La solución debe ser entregada en un archivo .py que se ejecute 
correctamente en el terminal de tu entorno de desarrollo.
"""

# SOLUCION

# Definición de la función principal
def main():
    # Solicitar al usuario que ingrese un número entero
    numero = int(input("Ingresa un número entero: "))

    # Condicional para verificar si el número es positivo, negativo o cero
    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")

# Llamada a la función principal
if __name__ == "__main__":
    main()
