"""
Ejercicio 73: True / False

Crear una función que reciba un carácter y determine si es una vocal, 
retornando True si lo es y False en caso contrario.

Agregar comentarios del funcionamiento del código del ejemplo a desarrollar. Asegúrate de que 
tu solución esté encapsulada en un archivo ejecutable con extensión .py
"""


#SOLUCIÓN

def vocal(caracter):
    """
    Función que determina si un carácter es una vocal o no.
    
    Parámetros:
    - caracter: carácter a evaluar
    - Retorna: True si el carácter es una vocal, False en caso contrario.
    """
    # Convertimos el carácter a minúscula para hacer la comparación más sencilla
    caracter = caracter.lower()
    
    # Comprobamos si el carácter es una vocal
    if caracter in 'aeiou':
        return True
    else:
        return False

# Ejemplo
if __name__ == "__main__":
    caracter = input("Ingrese un carácter: ")
    
    if len(caracter) == 1:
        if vocal(caracter):
            print("El carácter ingresado es una vocal.")
        else:
            print("El carácter ingresado no es una vocal.")
    else:
        print("Debe ingresar exactamente un carácter.")