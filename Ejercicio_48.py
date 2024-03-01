"""Ejercicios de Ficheros: Desarrollar un programa para gestionar un directorio telefónico de clientes de una empresa. El programa permitirá crear, buscar, agregar y eliminar información de clientes en un archivo de texto llamado directorio.txt, donde cada entrada contendrá el nombre y el número de teléfono del cliente separados por comas."""

def get_phone(file, client):
    '''
    Función que devuelve el teléfono de un cliente de un fichero dado.
    Parámetros:
        file: Nombre del fichero.
        client: Nombre del cliente.
    Devuelve:
        El teléfono del cliente o un mensaje de error.
    '''
    try: 
        with open(file, 'r') as f:
            directory = dict([tuple(line.split(',')) for line in f.readlines()])
            return directory.get(client, '¡El cliente {} no existe!\n'.format(client))
    except FileNotFoundError:
        return('¡El fichero {} no existe!\n'.format(file))


def add_phone(file, client, telf):
    '''
    Función que añade el teléfono de un cliente a un fichero.
    Parámetros:
        file: Nombre del fichero.
        client: Nombre del cliente.
        telf: Teléfono del cliente.
    Devuelve:
        Un mensaje indicando si el teléfono se ha añadido o no.
    '''
    try: 
        with open(file, 'a') as f:
            f.write(client + ',' + telf + '\n')
            return 'El teléfono se ha añadido.\n'
    except FileNotFoundError:
        return('¡El fichero {} no existe!\n'.format(file))


def remove_phone(file, client):
    '''
    Función que elimina el teléfono de un cliente de un fichero.
    Parámetros:
        file: Nombre del fichero.
        client: Nombre del cliente.
    Devuelve:
        Un mensaje indicando si el cliente se ha borrado o no.
    '''
    try: 
        with open(file, 'r') as f:
            directory = dict([tuple(line.split(',')) for line in f.readlines()])
            if client in directory:
                del directory[client]
                with open(file, 'w') as f:
                    for name, telf in directory.items():
                        f.write(name + ',' + telf)
                    return '¡El cliente se ha borrado!\n'
            else:
                return('¡El cliente {} no existe!\n'.format(client))
    except FileNotFoundError:
        return('¡El fichero {} no existe!\n'.format(file))


def create_directory(file):
    '''
    Función que crea un fichero para guardar un listín telefónico.
    Parámetros:
        file: Nombre del fichero.
    Devuelve:
        Un mensaje indicando si el fichero se ha creado correctamente o no.
    '''
    import os
    if os.path.isfile(file):
        answer = input('El fichero {} ya existe. ¿Desea vaciarlo (S/N)? '.format(file))
        if answer == 'N': 
            return 'No se ha creado el fichero porque ya existe.\n'
    with open(file, 'w') as f:
        return 'Se ha creado el fichero.\n'


def menu():
    '''
    Función que muestra un menú de operaciones para la gestión del listín telefónico.
    Devuelve:
        La opción seleccionada por el usuario.
    '''
    print('Gesión del listín telefónico')
    print('============================')
    print('1 - Consultar un teléfono')
    print('2 - Añadir un teléfono')
    print('3 - Eliminar un teléfono')
    print('4 - Crear el listín')
    print('0 - Terminar')
    return input('Introduzca el número de la opción deseada: ')


def directory():
    '''
    Función que ejecuta la aplicación para la gestión del listín telefónico.
    '''
    file = 'listin.txt' 
    while True:
        option = menu()
        if option == '1':
            name = input('Introduce el nombre del cliente: ')
            print(get_phone(file, name))
        elif option == '2':
            name = input('Introduce el nombre del cliente: ')
            telf = input('Introduce el teléfono del cliente: ')
            print(add_phone(file, name, telf))
        elif option == '3':
            name = input('Introduce el nombre del cliente: ')
            print(remove_phone(file, name))
        elif option == '4':
            print(create_directory(file))
        else:
            break

directory()
