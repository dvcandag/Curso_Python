# Ejercicio 17: Calcular el promedio de una lista de números:



# pide ingresar un números separados por espacios
numeros = input("Ingrese una lista de números separados por espacios: ")

# Convertir la entrada en una lista de números
numeros = [float(numero) for numero in numeros.split()]

# Calcular el promedio de los números
promedio = sum(numeros) / len(numeros)

# Imprimir el resultado
print("El promedio de los números es:", promedio)
