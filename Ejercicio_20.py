# Ejercicio 20: Ingresar una lista de números hasta que ingrese el número 0 para terminar. Luego, 
# calcular la suma y el promedio de los números ingresados y muestrar por pantalla.



numeros = []
numero = int(input("Ingrese un número (0 para terminar): "))

# Mientras el número ingresado no sea 0, continua pidiendo números y agregándolos a la lista.
while numero != 0:
    numeros.append(numero)
    numero = int(input("Ingrese un número (0 para terminar): "))

# Calcular la suma de los números en la lista.
suma = sum(numeros)
# Calcula el promedio dividiendo la suma entre la cantidad de números en la lista.
promedio = suma / len(numeros)

# Muestra la suma y el promedio de los números.
print("La suma de los números es:", suma)
print("El promedio de los números es:", promedio)


# Resultado:
# Ingrese un número (0 para terminar): 3434332
# Ingrese un número (0 para terminar): 23
# Ingrese un número (0 para terminar): 2343
# Ingrese un número (0 para terminar): 2
# Ingrese un número (0 para terminar): 32
# Ingrese un número (0 para terminar): 0
# La suma de los números es: 3471074
# El promedio de los números es: 578512.3333333334