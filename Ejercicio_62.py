"""
Ejercicio 18: Sumar intervalo del arreglo.

Crea una función denominada (sumarArreglo) que requiera tres argumentos: un arreglo de números, 
la posición inicial y la posición final. La función debe devolver la suma de todos los números 
dentro del rango especificado, incluyendo tanto la posición inicial como la posición final.

Nota: Se puede asumir que la posición inicial será menor o igual que la posición final, y 
que ambas estarán dentro de los límites del arreglo [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"

Proporcionar comentarios explicativos. Tu solución debe entregarse en un archivo .py 
que se ejecute en el terminal mostrando como salida 18

"""
# Definición de la función sumar_arreglo que suma los elementos dentro de un rango específico de una lista
def sumar_arreglo(arr, inicio, fin):
    # Inicializamos una variable para almacenar la suma
    suma = 0
    # Recorrer la lista desde la posición de inicio hasta la posición de fin
    for i in range(inicio, fin + 1):
        # Sumar el elemento actual al total
        suma += arr[i]
    # Retornar la suma de los elementos dentro del rango especificado
    return suma

# Mostrando la salida:
arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Definir una lista
inicio = 2  # Definir la posición de inicio
fin = 5  # Definir la posición de fin
resultado = sumar_arreglo(arreglo, inicio, fin)  # Llamar a la función sumar_arreglo
print(resultado)  # Imprimir el resultado de la suma
# Salida esperada: 18 (3 + 4 + 5 + 6 = 18)
