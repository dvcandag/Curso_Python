"""
Ejercicio 60:
Desarrollar un software para administrar un directorio telefónico que contenga los nombres y números de teléfono 
de los clientes de una empresa. El programa incluirá funciones para crear el archivo del directorio en caso de que 
no exista, para consultar el número de teléfono de un cliente, agregar el número de teléfono de un nuevo cliente y 
eliminar el número de teléfono de un cliente existente. El directorio se almacenará en un archivo de texto llamado 
listin.txt, donde el nombre del cliente y su número de teléfono estarán separados por comas, y cada cliente 
ocupará una línea individual.

"""


#SOLUCION

import os

def crear_listin(nombre_fichero):
   
    if not os.path.exists(nombre_fichero):
        with open(nombre_fichero, 'w') as file:
            pass  # Crea el fichero vacío si no existe

def consultar_telefono(nombre_fichero, nombre_cliente):
   
    with open(nombre_fichero, 'r') as file:
        for line in file:
            nombre, telefono = line.strip().split(',')
            if nombre == nombre_cliente:
                return telefono
    return "El cliente no está en el listín."

def agregar_telefono(nombre_fichero, nombre_cliente, telefono):
  
    with open(nombre_fichero, 'a') as file:
        file.write(f"{nombre_cliente},{telefono}\n")

def eliminar_telefono(nombre_fichero, nombre_cliente):

    with open(nombre_fichero, 'r') as file:
        lines = file.readlines()

    with open(nombre_fichero, 'w') as file:
        for line in lines:
            nombre, _ = line.strip().split(',')
            if nombre != nombre_cliente:
                file.write(line)

# Nombre del fichero del listín
nombre_fichero = "listin.txt"

# Crear el fichero con el listín si no existe
crear_listinte(nombre_fichero)

# Ejemplo de uso:
agregar_telefono(nombre_fichero, "Vito", "123456789")
agregar_telefono(nombre_fichero, "María", "987654321")
print("Teléfono de Vito:", consultar_telefono(nombre_fichero, "Vito"))
print("Teléfono de María:", consultar_telefono(nombre_fichero, "María"))

# Eliminar el teléfono de Vito
eliminar_telefono(nombre_fichero, "Vito")
print("Teléfono de Vito después de eliminar:", consultar_telefono(nombre_fichero, "Vito"))
