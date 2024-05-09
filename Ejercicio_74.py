"""
Ejercicio 74: Histograma
Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. 
Ejemplo: procedimiento([3, 7, 5]) debería imprimir lo siguiente:

***
*******
*****

"""
#SOLUCIÓN

def histograma_procedimiento(lista_numeros):
 for numero in lista_numeros:
        print('*' * numero)

# Ejemplo de uso
histograma_procedimiento([3, 7, 5])