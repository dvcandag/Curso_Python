"""
Ejercicio 57:
Se centra en la creación y manipulación de listas, explorando diversas formas de 
inicialización y acceso a elementos. Se muestra la flexibilidad de las listas al permitir 
la inclusión de elementos de diferentes tipos de datos en una sola lista.

Instrucciones:
1.- Analizar y comprender las distintas formas de inicializar listas, como asignación de valores 
individuales, multiplicación de elementos y inclusión de elementos de diferentes tipos de datos.
2.- Ejecutar el código proporcionado para observar los resultados de acceder a los elementos de cada lista.
3.- Experimentar con la manipulación de listas, incluyendo la modificación de elementos existentes y la inclusión de nuevos elementos.
4.- Reflexionar sobre las ventajas de utilizar listas y su aplicabilidad en diversos escenarios de programación.

Proporcionar comentarios explicativos. Tu solución debe entregarse en un archivo .py

"""

# Creación de listas en Python
vector1 = [None]  # Creación de una lista con un elemento None
vector1[0] = 1  # Modificación del primer elemento de la lista

vector2 = [None]  # Creación de otra lista con un elemento None
vector2[0] = 6  # Modificación del primer elemento de la segunda lista

vector3 = [None] * 5  # Creación de una lista con cinco elementos None
vector3[0] = 4  # Modificación del primer elemento de la tercera lista

vector4 = [3, 70, 'Vitto Andagua']  # Creación de una lista con elementos 1, 70 y 'juan'
vector5 = [1, 70, 'Juan Lozada']  # Creación de otra lista con los mismos elementos que la anterior

# Imprimir elementos de las listas
print(vector1[0])  # Imprimir el primer elemento de la lista vector1
print(vector2[0])  # Imprimir el primer elemento de la lista vector2
print(vector3[0])  # Imprimir el primer elemento de la lista vector3
print(vector4[0])  # Imprimir el primer elemento de la lista vector4
print(vector5[0])  # Imprimir el primer elemento de la lista vector5

