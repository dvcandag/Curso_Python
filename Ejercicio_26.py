# Ejercicio 26: ingresar una cadena por input y mostrar el reverso de cadena

def reverso_cadena(cadena):
    return cadena[::-1]

cadena_usuario = input("Ingresa una cadena: ")
print("Reverso de la cadena:", reverso_cadena(cadena_usuario))
