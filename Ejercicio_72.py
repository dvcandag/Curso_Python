"""
Ejercicio 72: función len()

Crear una función que determine la extensión de una lista o cadena específica es una práctica valiosa, 
a pesar de que Python ya incluya la función len() de manera predeterminada.

Agregar comentarios del funcionamiento del código del ejemplo a desarrollar. Asegúrate de que 
tu solución esté encapsulada en un archivo ejecutable con extensión .py

"""


# SOLUCIÓN

# Definimos la función len para calcular la longitud de una lista o cadena dada

def len(objeto):
    """
    Calcula la longitud de una lista o cadena dada.
    
    objeto: lista o cadena de la cual se desea calcular la longitud.
    longitud: entero que representa la longitud del objeto.
    """
    longitud = 0  # Inicializamos la longitud en 0
    
    # Iteramos sobre los elementos del objeto y contamos cada uno
    for _ in objeto:
        longitud += 1
    
    return longitud

# Ejemplos de uso de la función len
if __name__ == "__main__":
    lista_ejemplo = [1, 2, 3, 4, 4]
    cadena_ejemplo = "Hola, soy Vitto!"
    
    print("Longitud de la lista:", len(lista_ejemplo))  # Salida esperada: 5
    print("Longitud de la cadena:", len(cadena_ejemplo))  # Salida esperada: 12

