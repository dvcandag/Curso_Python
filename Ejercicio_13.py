# Ejercicio 13: Contar la cantidad de letras de cadena

def contar_letras(cadena):
    # Inicializar un diccionario para almacenar el conteo de letras
    conteo_letras = {}
    # Iterar sobre cada letra en la cadena
    for letra in cadena:
        # Verificar si la letra ya está en el diccionario
        if letra in conteo_letras:
            # Incrementar el conteo de la letra si ya está en el diccionario
            conteo_letras[letra] += 1
        else:
            # Agregar la letra al diccionario con un conteo inicial de 1 si no está presente
            conteo_letras[letra] = 1
    return conteo_letras

# Ejemplo de uso:
cadena = "Hola, mundo!"
print("Conteo de letras en la cadena:", contar_letras(cadena))
