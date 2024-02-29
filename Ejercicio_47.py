"""Ejercicios de Ficheros: Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero 
tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. 
Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello"""

def mostrar_linea_tabla():
    try:
        n = int(input('Introduce un número entero entre 1 y 10: '))
        m = int(input('Introduce otro número entero entre 1 y 10: '))
        
        if 1 <= n <= 10 and 1 <= m <= 10:
            nombre_fichero = 'tabla-' + str(n) + '.txt'
            try:
                with open(nombre_fichero, 'r') as f:
                    lineas = f.readlines()
                    if len(lineas) >= m:
                        print(lineas[m - 1].strip())
                    else:
                        print("La tabla de multiplicar para", n, "no tiene", m, "líneas.")
            except FileNotFoundError:
                print("El archivo", nombre_fichero, "no existe. Creando archivo...")
                with open(nombre_fichero, 'w') as f:
                    for i in range(1, 11):
                        f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
                print("Archivo", nombre_fichero, "creado. La tabla de multiplicar se ha guardado.")
        else:
            print("Los números ingresados están fuera del rango permitido.")
    except ValueError:
        print("Por favor, introduce números enteros válidos.")


mostrar_linea_tabla()

