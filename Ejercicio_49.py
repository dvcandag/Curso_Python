"""Ejercicio 49: Desarrollar un programa que solicite al usuario ingresar datos de ventas 
durante varios años, luego, el programa mostrará un gráfico de líneas 
que ilustra la evolución de estas ventas a lo largo del tiempo."""

import matplotlib.pyplot as plt

# Preguntamos por el año inicial
while True:
    try:
        inicio = int(input('Introduce el año inicial: '))
        break
    except ValueError:
        print("Por favor, introduce un año válido.")

# Preguntamos por el año final
while True:
    try:
        fin = int(input('Introduce el año final: '))
        if fin >= inicio:
            break
        else:
            print("El año final debe ser mayor o igual que el año inicial.")
    except ValueError:
        print("Por favor, introduce un año válido.")

# Definimos un diccionario vacío para guardar las ventas de cada año
ventas = {}

# Bucle iterativo para preguntar las ventas de cada año y guardarlas en el diccionario
for i in range(inicio, fin+1):
    while True:
        try:
            ventas[i] = float(input('Introduce las ventas del año ' + str(i) +': '))
            break
        except ValueError:
            print("Por favor, introduce un número válido.")

# Definimos la figura y los ejes del gráfico con Matplotlib
fig, ax = plt.subplots()

# Dibujamos la línea con las ventas a partir del diccionario
ax.plot(ventas.keys(), ventas.values())

# Añadimos etiquetas
ax.set_xlabel('Año')
ax.set_ylabel('Ventas')

# Añadimos título
ax.set_title('Ventas por año')

# Mostramos el gráfico por pantalla
plt.show()
