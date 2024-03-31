"""
Ejercicio 67: Función superposicion()
    
Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro 
en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado

Proporcionar comentarios explicativos. Tu solución debe ejecutarse  ejemplos y entregarse en un archivo .py

"""

#SOLUCION

def superposicion(lista1, lista2):
    # Iterar sobre cada elemento de la primera lista
    for elemento1 in lista1:
        # Iterar sobre cada elemento de la segunda lista
        for elemento2 in lista2:
            # Comprobar si hay al menos un elemento en común
            if elemento1 == elemento2:
                return True
    # Si no se encuentra ninguna superposición, devolver False
    return False

# Ejemplo 1 - false
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
print(superposicion(lista1, lista2))  # Output: False


# Ejemplo 2 - true
lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 6, 7, 8, 9]
print(superposicion(lista1, lista2))  # Output: True