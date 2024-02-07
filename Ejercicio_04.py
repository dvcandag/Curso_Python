# Ingresar una palabra
palabra = input("Ingrese una palabra: ")

# Verifica si la palabra es un palíndromo
es_palindromo = palabra == palabra[::-1]

# Imprimir el resultado
if es_palindromo:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
