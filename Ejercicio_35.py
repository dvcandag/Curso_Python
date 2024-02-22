# Ejercicio 35: Crear un programa que elimine todos los elementos duplicados de una lista.
 

def eliminar_duplicados(lista):
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados

# Solicitar al usuario que ingrese los elementos de la lista separados por comas
entrada = input("Ingresa los elementos de la lista separados por comas: ")

# Convertir la entrada en una lista separando por comas y eliminando los espacios en blanco
mi_lista = [int(x.strip()) for x in entrada.split(',')]

# Eliminar duplicados
lista_sin_duplicados = eliminar_duplicados(mi_lista)

# Imprimir la lista sin duplicados
print("Lista original:", mi_lista)
print("Lista sin duplicados:", lista_sin_duplicados)
