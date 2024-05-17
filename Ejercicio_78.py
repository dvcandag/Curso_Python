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

# Función principal del programa
def main():
    try:
        # Solicitamos al usuario que ingrese las longitudes de los lados del triángulo
        lado1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
        lado2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
        lado3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))
        
        # Comprobamos si los valores ingresados son válidos
        if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
            print("Error: Los lados del triángulo deben ser mayores que cero.")
        # Comprobamos si las longitudes ingresadas forman un triángulo válido
        elif lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
            print("Error: Las longitudes de los lados no forman un triángulo válido.")
        else:
            # Llamamos a la función para determinar el tipo de triángulo y mostramos el resultado
            tipo = tipo_triangulo(lado1, lado2, lado3)
            print(f"El triángulo es {tipo}.")
    except ValueError:
        print("Error: Ingrese valores numéricos válidos para los lados del triángulo.")

# Verificamos si este archivo es el punto de entrada principal del programa
if __name__ == "__main__":
    main()
