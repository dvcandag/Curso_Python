# Ejercicio 23: Empleando una función llamada largo_cadena que tome un argumento y devuelva 
# la cantidad de elementos que contiene. Luego, prueba esta función con una lista
# y una cadena de texto como argumentos diferentes.


def largo_cadena(lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont
# con lista:  los espacios no cuentan como elementos individuales en una lista de Python
print(largo_cadena([1, 2, 3, 4, 2, 0]))
# con cadena: la función cuenta cada carácter, incluyendo letras, espacios y signos de puntuación
print(largo_cadena("hola, como leva?"))
