# Ejercicio 11: Contar Vocales, ingresado por función input()
 
def contar_vocales(cadena):
    # Inicializar un contador para las vocales
    contador_vocales = 0
    # Iterar o recorrer sobre cada caracter en la cadena
    for caracter in cadena:
        # Verificar si el caracter es una vocal (en minúsculas o mayúsculas)
        if caracter.lower() in 'aeiou':
            contador_vocales += 1
    return contador_vocales

# Solicitar al usuario que ingrese una cadena
cadena = input("Ingrese una cadena: ")
# Llamar a la función contar_vocales con la cadena ingresada por el usuario
print("Número de vocales en la cadena:", contar_vocales(cadena))
