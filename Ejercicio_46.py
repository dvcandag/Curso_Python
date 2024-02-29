"""Ejercicios de Ficheros:pida un número entero entre 1 y 10 y guarde 
en un fichero con el nombre tabla-n.txt la tabla de multiplicar 
de ese número, done n es el número introducido.
"""

try:
    n = int(input('Introduce un número entero entre 1 y 10: '))
    if 1 <= n <= 10:
        nombre_fichero = 'tabla-' + str(n) + '.txt'
        with open(nombre_fichero, 'w') as f:
            for i in range(1, 11):
                f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
        print("La tabla de multiplicar se ha guardado en el archivo", nombre_fichero)
    else:
        print("El número ingresado está fuera del rango permitido.")
except ValueError:
    print("Por favor, introduce un número entero válido.")
