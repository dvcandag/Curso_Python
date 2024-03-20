"""
Ejercicio 19: Generar contraseña

Desarrollar una función denominada (password) que tome un string como entrada y 
devuelva otro string con los siguientes cambios realizados:

a.- Convertir las mayúsculas a minúsculas.
b.- Eliminar los espacios en blanco.
c.- Reemplazar el carácter 'a' por '4'.
d.- Reemplazar el carácter 'e' por '3'.
e.- Reemplazar el carácter 'i' por '1'.
f.- Reemplazar el carácter 'o' por '0'."

Proporcionar comentarios explicativos. Tu solución debe entregarse en un archivo .py 
ejecutandose satisfactoriamente en el terminal de su entorno de desarrollo.
"""

#SOLUSION

# Definición de la función 'password' para generar una contraseña modificada
def password(string):
    # Convertir todas las letras a minúsculas y eliminar espacios en blanco
    string = string.lower().replace(' ', '')

    # Reemplazar caracteres específicos según las reglas
    string = string.replace('a', '4')  # Reemplazar 'a' por '4'
    string = string.replace('e', '3')  # Reemplazar 'e' por '3'
    string = string.replace('i', '1')  # Reemplazar 'i' por '1'
    string = string.replace('o', '0')  # Reemplazar 'o' por '0'

    return string  # Devolver la contraseña modificada

# Función para generar la contraseña y mostrarla en la consola
def generar_password():
    # Obtener la contraseña ingresada por el usuario
    entrada = input("Ingrese la contraseña: ")
    # Generar la contraseña modificada usando la función 'password'
    resultado = password(entrada)
    # Mostrar la contraseña generada en la consola
    print("Contraseña generada:", resultado)

# Llamar a la función para generar la contraseña
generar_password()
