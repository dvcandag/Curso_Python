"""
Ejercicio 80: Mayor de edad

Crea un programa en Python que determine si una persona es mayor de edad o no, basado en la edad ingresada por el usuario. El programa debe 
solicitar al usuario que ingrese su edad y luego determinar si es mayor o igual a 18 años, considerando esta como la mayoría de edad. El programa 
debe imprimir un mensaje indicando si la persona es mayor de edad o no. Asegúrate de manejar correctamente situaciones donde se ingresen valores 
no válidos para la edad, como letras o números negativos.
"""

# SOLUCIÓN

def es_mayor_de_edad():
    try:
        edad = int(input("Por favor, ingresa tu edad: "))
        if edad >= 18:
            print("Eres mayor de edad.")
        else:
            print("Eres menor de edad.")
    except ValueError:
        print("Error: Por favor ingresa un valor numérico válido para la edad.")

es_mayor_de_edad()
