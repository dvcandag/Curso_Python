 # Ejercicio 10: Verificar Palíndromos

def es_palindromo(cadena):
    # Convertir la cadena a minúsculas y eliminar espacios y puntuación
    cadena = cadena.lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    # Verificar si la cadena es igual a su inversa
    return cadena == cadena[::-1]

# Ejemplo 1:
cadena = "Anita lava la tina."
print("¿Es un palíndromo?", es_palindromo(cadena))

# Ejemplo 2:
cadena = "Anita no lava la tina."
print("¿Es un palíndromo?", es_palindromo(cadena))
