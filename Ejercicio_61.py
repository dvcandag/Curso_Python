"""
Ejercicio 17: Remover ceros
Desarrollar una función denominada (removerCeros) la cual acepta un arreglo 
de números como argumento y devuelve un nuevo arreglo que excluye todos 
los ceros (0) del arreglo original [4, 0, 5, 0, 2, 0, 5]

Proporcionar comentarios explicativos. Tu solución debe entregarse en un archivo .py 
que se ejecute en el terminal mostrando la salida: [4, 5, 2, 5]
"""

#SOLUCION
# Definición de la función remover_ceros que elimina los ceros de una lista
def remover_ceros(arr):
    # Utiliza una list comprehension para crear una nueva lista que excluya los ceros
    return [num for num in arr if num != 0]

# Mostrando la salida:
arreglo_original = [4, 0, 5, 0, 2, 0, 5]  # Lista original que contiene ceros
arreglo_sin_ceros = remover_ceros(arreglo_original)  # Llama a la función remover_ceros
print(arreglo_sin_ceros)  # Imprime la nueva lista sin los ceros: [4, 5, 2, 5]
