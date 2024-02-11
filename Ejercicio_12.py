# Ejercicio 12: Contar palabras

def contar_palabras(cadena):
    # Dividir la cadena en palabras usando espacios en blanco como delimitadores
    palabras = cadena.split()
    # Contar el número de palabras en la lista resultante
    return len(palabras)

# Ejemplo de uso:
cadena = "Hola,soy Vitto ¿cómo estás?"
print("Número de palabras en la cadena:", contar_palabras(cadena))
