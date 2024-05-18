"""
Ejercicio 81: número total de dígitos

Dado un número, cuente el número total de dígitos de un número
"""
# SOLUCIÓN

def contar_digitos(numero):
    # Convertir el número en una cadena y contar los caracteres
    return len(str(numero))

# Solicitar al usuario que ingrese un número
numero = input("Por favor, ingresa un número: ")

# Verificar si el usuario ingresó un número válido
if numero.isdigit():
    # Convertir el número ingresado a entero y contar los dígitos
    total_digitos = contar_digitos(int(numero))
    print("El número total de dígitos en", numero, "es:", total_digitos)
else:
    print("Por favor, ingresa un número válido.")
